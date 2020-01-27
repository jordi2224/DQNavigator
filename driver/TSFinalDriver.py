'''Animates distances and measurment quality'''
import codecs

from rplidar import RPLidar
import matplotlib.pyplot as plt
import numpy as np
import numpy.matlib as npm
import matplotlib.animation as animation
import serial
import sys
import time
import matplotlib.pyplot as plt
import math
import pandas as pd
from sklearn.cluster import KMeans

DESCRIPTOR_LEN = 7
INFO_LEN = 20
HEALTH_LEN = 3

INFO_TYPE = 4
HEALTH_TYPE = 6
SCAN_TYPE = 129

SYNC_BYTE = b'\xA5'
SYNC_BYTE2 = b'\x5A'
GET_LIDAR_CONF = b'\x84'
GET_HEALTH_BYTE = b'\x52'
GET_INFO_BYTE = b'\x50'

EXPRESS_SCAN = b'\x82'
SCAN_BYTE = b'\x20'

MAX_SAMPLES_PER_SCAN = 50

_HEALTH_STATUSES = {
    0: 'Good',
    1: 'Warning',
    2: 'Error',
}

STOP_BYTE = b'\x25'


def _b2i(byte):
    '''Converts byte to integer (for Python 2 compatability)'''
    return byte if int(sys.version[0]) == 3 else ord(byte)


def send_cmd(ser, cmd):
    ser.write(SYNC_BYTE + cmd)


def read_descriptor(ser, debug=0):
    '''Reads descriptor packet'''
    descriptor = ser.read(7)
    if (debug): print('Recieved descriptor: ', "".join('{:02x} '.format(x) for x in descriptor))
    if len(descriptor) != 7:
        print(len(descriptor))
        raise Exception('Descriptor length mismatch')
    elif not descriptor.startswith(SYNC_BYTE + SYNC_BYTE2):
        raise Exception('Incorrect descriptor starting bytes')
    is_single = _b2i(descriptor[-2]) == 0
    '''size = _b2i(descriptor[2]) + (_b2i(descriptor[3]) << 8) + (_b2i(descriptor[4]) << 8) + (
                (_b2i(descriptor[5]) & ord(b'\x3F')) << 8)'''
    return _b2i(descriptor[2]), is_single, _b2i(descriptor[-1])


def read_response(ser, dsize):
    '''Reads response packet with length of `dsize` bytes'''
    data = ser.read(dsize)
    if len(data) != dsize:
        raise Exception('Wrong body size')
    return data


def get_health(ser):
    ser.write(SYNC_BYTE + GET_HEALTH_BYTE)
    dsize, is_single, dtype = read_descriptor(ser)
    if dsize != HEALTH_LEN:
        raise Exception('Wrong get_health reply length')
    if not is_single:
        raise Exception('Not a single response mode')
    if dtype != HEALTH_TYPE:
        raise Exception('Wrong response data type')
    raw = read_response(ser, dsize)
    status = _HEALTH_STATUSES[_b2i(raw[0])]
    return status


def get_info(ser):
    ser.write(SYNC_BYTE + GET_INFO_BYTE)
    dsize, is_single, dtype = read_descriptor(ser)
    if dsize != INFO_LEN:
        raise Exception('Wrong get_info reply length')
    if not is_single:
        raise Exception('Not a single response mode')
    if dtype != INFO_TYPE:
        raise Exception('Wrong response data type')

    raw = read_response(ser, dsize)
    serialnumber = codecs.encode(raw[4:], 'hex').upper()
    serialnumber = codecs.decode(serialnumber, 'ascii')
    data = {
        'model': _b2i(raw[0]),
        'firmware': (_b2i(raw[2]), _b2i(raw[1])),
        'hardware': _b2i(raw[3]),
        'serialnumber': serialnumber,
    }
    return data


def prepare_payload(cmd_type, payload):
    checksum = 0;
    checksum = checksum ^ ord(SYNC_BYTE)
    checksum = checksum ^ ord(cmd_type)
    checksum = checksum ^ len(payload)
    for byte in payload:
        checksum = checksum ^ byte

    return bytes(SYNC_BYTE) + cmd_type + bytes([len(payload)]) + payload + bytes([checksum])


def get_mode_count(ser):
    ser.write(prepare_payload(GET_LIDAR_CONF, b'\x70\x00\x00\x00'))
    dsize, none, none = read_descriptor(ser)
    raw = read_response(ser, dsize)
    count = raw[4]
    return count


def get_mode_name(ser, mode):
    ser.write(prepare_payload(GET_LIDAR_CONF, b'\x7f\x00\x00\x00' + bytes([mode]) + b'\x00'))
    dsize, none, none = read_descriptor(ser)
    raw = read_response(ser, dsize)
    return raw[4:].decode('utf-8')


def stop(ser):
    ser.write(SYNC_BYTE + STOP_BYTE)
    ser.read_all()
    ser.drt = True


def initial_debug(ser):
    print('Starting RPLIDAR checks:')
    stop(ser)
    time.sleep(0.2)
    stop(ser)
    print("Device info: " + str(get_info(ser)))
    print("Device health: " + get_health(ser))
    print("Sensor supports the following modes:")

    mode_count = get_mode_count(ser)
    for mode in range(mode_count):
        print(str(mode) + ":  " + get_mode_name(ser, mode))


def start_scan_express(ser):
    ser.dtr = False
    ser.write(prepare_payload(EXPRESS_SCAN, b'\x00 + 'b'\x00' * 4))
    dsize, none, none = read_descriptor(ser, debug=1)
    return dsize


def start_scan(ser):
    ser.dtr = False
    ser.write(SYNC_BYTE + SCAN_BYTE)
    dsize, none, none = read_descriptor(ser, debug=1)
    return dsize


def get_express(ser, dsize):
    bytes_in = ser.read(dsize)
    received_sync = (bytes_in[0] & 240) + (bytes_in[1] >> 4)
    if (received_sync != ord(SYNC_BYTE)):
        raise BufferError("Mismatching Sync bytes")
    else:
        ultra_cabins = []
        start_angle = (bytes_in[2] + ((bytes_in[3] & 127) << 8)) / 64.0
        for i in range(len(bytes_in[4:]) // 5):
            ultra_cabins.append(bytes_in[4 + i * 5: 4 + (i + 1) * 5])

    return ultra_cabins, start_angle


def parse_cabins(cabins, start_angle, diffAngle, do_compensation=0):
    angle = start_angle
    points = []
    for cabin in cabins:
        distance1 = ((cabin[0] >> 2) + (cabin[1] << 6))
        distance2 = ((cabin[2] >> 2) + (cabin[3] << 6))
        dt1 = ((cabin[4] & 15) + ((cabin[0] & 3) << 4))
        dt2 = (((cabin[4] & 240) >> 4) + ((cabin[2] & 3) << 4))

        if (do_compensation):
            if (dt1 >> 5):
                dt1 = -(dt1 & 31)
            else:
                dt1 = (dt1 & 31)
            if (dt2 >> 5):
                dt2 = -(dt1 & 31)
            else:
                dt2 = (dt2 & 31)

            angle += diffAngle / 32.0
            points.append((math.radians((angle + dt1 / 32.0) % 360.0), distance1))
            angle += diffAngle / 32.0
            points.append((math.radians((angle + dt2 / 32.0) % 360.0), distance2))
        else:
            angle += diffAngle / 32.0
            points.append((math.radians((angle) % 360.0), distance1))
            angle += diffAngle / 32.0
            points.append((math.radians((angle) % 360.0), distance2))

    return points


def parse_scan(ser):
    samples = []

    i = 0
    while ((ser.in_waiting > 5) and (i < MAX_SAMPLES_PER_SCAN)):
        bytes_in = ser.read(5)
        quality = bytes_in[0] >> 2
        angle = ((bytes_in[1] >> 1) + (bytes_in[2] << 7)) / 64.0
        distance = (bytes_in[3] + (bytes_in[4] << 8)) / 4.0
        samples.append((math.radians(angle), distance))
        i += 1

    return samples


def get_points(max_distance, samples):
    x_points = []
    y_points = []
    for i in range(len(samples)):
        sample = samples[i]
        if (sample[1] < max_distance and sample[1] != 0.0):
            y_points.append(math.cos(sample[0]) * sample[1])
            x_points.append(math.sin(sample[0]) * sample[1])
    return x_points, y_points


def get_notes(centers, table_divisions):
    step = 360.0 / float(table_divisions)
    polar = []
    notes = [0] * table_divisions
    for center in centers:
        angle = math.degrees(math.atan2(center[1], center[0]))
        distance = math.sqrt(math.pow(center[0], 2) + math.pow(center[1], 2))
        if (distance > 50):
            polar.append((angle, distance))
    for division in range(table_divisions):
        notes_in_range = []
        lower = -180 + step * division
        higher = -180 + step * (division + 1)
        for point in polar:
            if (point[0] >= lower and point[0] < higher):
                notes_in_range.append(point[1])

        #if (len(notes_in_range) > 1 and (max(notes_in_range) - min(notes_in_range)) < 100):
        if (len(notes_in_range) > 1 ):
            notes[division] = min(notes_in_range)
        else:
            notes[division] = 0

    return notes


def renormalize(n, range1, range2):
    delta1 = range1[1] - range1[0]
    delta2 = range2[1] - range2[0]
    return (delta2 * (n - range1[0]) / delta1) + range2[0]


def crush_notes(notes, max_distance, min_distance, n_notes):
    crushed_notes = b''
    for note in notes:
        note = int(renormalize(note, (min_distance, max_distance), (2, n_notes + 1)))
        crushed_notes += bytes([note])

    # print(crushed_notes)
    return crushed_notes


def main():
    print("Starting RPLIDAR on port: " + sys.argv[1])
    '''
    ser = serial.Serial(sys.argv[1], 115200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, dsrdtr=False,
                        timeout=1)
    ser.read_all()
    ser.close()
    ser.open()
    stop(ser)
    time.sleep(0.1)
    ser.read_all()
    '''

    print("Max connection on port: " + sys.argv[2])
    to_max = serial.Serial(sys.argv[2], 115200)
    to_max.close()
    to_max.open()
    to_max.read_all()

    table_divisions = 16

    print("Serial connections Ok!")
    print("Now waiting for Max...\n")
    while (to_max.in_waiting == 0):
        pass

    print("Found Max!")
    table_divisions = int.from_bytes(to_max.read(), "big")
    print("Starting scan for n = " + str(table_divisions))
    if (not table_divisions > 0):
        print("Oops! It seems like that number is invalid!")
        print("Defaulting to n = 16")
        table_divisions = 16

    dsize = start_scan_express(ser)
    print("Expecting samples of size: " + str(dsize))
    while (ser.in_waiting < dsize): pass
    old_cabins, old_start_angle = get_express(ser, dsize)

    print("Max distance will be set at: " + sys.argv[3] + "mm")
    max_distance = int(sys.argv[3])
    min_distane = 120
    n_notes = 12

    data_out_count = 0
    while True:
        x_points = []
        y_points = []
        datapoints = 0
        while (datapoints < 2000):

            if (to_max.in_waiting != 0):
                table_divisions = int.from_bytes(to_max.read(), "big")
                print("\nStarting scan for n = " + str(table_divisions))
                to_max.read_all()
                if (not table_divisions > 0):
                    print("Oops! It seems like that number is invalid!")
                    print("Defaulting to n = 16")
                    table_divisions = 16

            if (ser.in_waiting > dsize):
                new_cabins, new_start_angle = get_express(ser, dsize)
                if new_start_angle >= old_start_angle:
                    diffAngle = new_start_angle - old_start_angle
                else:
                    diffAngle = new_start_angle + 360.0 - old_start_angle

                points = parse_cabins(old_cabins, old_start_angle, diffAngle, do_compensation=0)
                datapoints += len(points)

                new_x_points, new_y_points = get_points(max_distance, points)
                x_points += new_x_points
                y_points += new_y_points
                old_cabins = new_cabins
                old_start_angle = new_start_angle
        points = []
        for i in range(len(x_points)):
            points.append((x_points[i], y_points[i]))
        notes = get_notes(points, table_divisions)
        # print(notes)
        data_out_count += 1
        print(".", end='')
        if (data_out_count % 40 == 0): print("")
        to_max.write(crush_notes(notes, max_distance, min_distane, n_notes))

    fig = plt.figure()
    ax = fig.gca()
    plt.axis([-max_distance, max_distance, -max_distance, max_distance])
    ax.scatter(x_points, y_points, s=1)
    # ax.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=10, c='r')

    ax.set_aspect('equal')
    plt.show()

    ser.dtr = True
    input()

    input()


if __name__ == '__main__':
    main()
