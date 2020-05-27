import codecs
import serial
import sys
import time
from driver.driver_tools import *


def _b2i(byte):
    """Converts byte to integer (for Python 2 compatability)"""
    return byte if int(sys.version[0]) == 3 else ord(byte)


class Driver:

    def __init__(self, port, check_info=True, check_health=True):
        self.connection = serial.Serial(port, 115200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,
                                        dsrdtr=False, timeout=1)
        self.stop()
        self.connection.close()
        self.connection.open()
        self.connection.read_all()

        if check_info:
            print(self.get_info())
        if check_health:
            print("Health: ", self.get_health())

    def send_cmd(self, cmd):
        self.connection.write(SYNC_BYTE + cmd)

    def read_descriptor(self, debug=0):
        """Reads descriptor packet"""
        descriptor = self.connection.read(7)
        if debug:
            print('Recieved descriptor: ', "".join('{:02x} '.format(x) for x in descriptor))
        if len(descriptor) != 7:
            print(len(descriptor))
            raise Exception('Descriptor length mismatch')
        elif not descriptor.startswith(SYNC_BYTE + SYNC_BYTE2):
            raise Exception('Incorrect descriptor starting bytes')
        is_single = _b2i(descriptor[-2]) == 0
        '''size = _b2i(descriptor[2]) + (_b2i(descriptor[3]) << 8) + (_b2i(descriptor[4]) << 8) + (
                    (_b2i(descriptor[5]) & ord(b'\x3F')) << 8)'''
        return _b2i(descriptor[2]), is_single, _b2i(descriptor[-1])

    def read_response(self, dsize):
        """Reads response packet with length of `dsize` bytes"""
        data = self.connection.read(dsize)
        if len(data) != dsize:
            raise Exception('Wrong body size')
        return data

    def get_health(self):
        self.connection.write(SYNC_BYTE + GET_HEALTH_BYTE)
        dsize, is_single, dtype = self.read_descriptor()
        if dsize != HEALTH_LEN:
            raise Exception('Wrong get_health reply length')
        if not is_single:
            raise Exception('Not a single response mode')
        if dtype != HEALTH_TYPE:
            raise Exception('Wrong response data type')
        raw = self.read_response(dsize)
        status = HEALTH_STATUSES[_b2i(raw[0])]
        return status

    def get_info(self):
        self.connection.write(SYNC_BYTE + GET_INFO_BYTE)
        dsize, is_single, dtype = self.read_descriptor()
        if dsize != INFO_LEN:
            raise Exception('Wrong get_info reply length')
        if not is_single:
            raise Exception('Not a single response mode')
        if dtype != INFO_TYPE:
            raise Exception('Wrong response data type')

        raw = self.read_response(dsize)
        serialnumber = codecs.encode(raw[4:], 'hex').upper()
        serialnumber = codecs.decode(serialnumber, 'ascii')
        data = {
            'model': _b2i(raw[0]),
            'firmware': (_b2i(raw[2]), _b2i(raw[1])),
            'hardware': _b2i(raw[3]),
            'serialnumber': serialnumber,
        }
        return data

    def get_mode_count(self):
        self.connection.write(prepare_payload(GET_LIDAR_CONF, b'\x70\x00\x00\x00'))
        dsize, none, none = self.read_descriptor()
        raw = self.read_response(dsize)
        count = raw[4]
        return count

    def get_mode_name(self, mode):
        self.connection.write(prepare_payload(GET_LIDAR_CONF, b'\x7f\x00\x00\x00' + bytes([mode]) + b'\x00'))
        dsize, none, none = self.read_descriptor()
        raw = self.read_response(dsize)
        return raw[4:].decode('utf-8')

    def stop(self):
        self.connection.write(SYNC_BYTE + STOP_BYTE)
        self.connection.read_all()
        self.connection.drt = True

    def initial_debug(self):
        print('Starting RPLIDAR checks:')
        self.stop()
        time.sleep(0.2)
        self.stop()
        print("Device info: " + str(self.get_info()))
        print("Device health: " + self.get_health())
        print("Sensor supports the following modes:")

        mode_count = self.get_mode_count()
        for mode in range(mode_count):
            print(str(mode) + ":  " + self.get_mode_name(mode))

    def start_scan_express(self):
        self.connection.dtr = False
        self.connection.write(prepare_payload(EXPRESS_SCAN, b'\x00 + 'b'\x00' * 4))
        dsize, none, none = self.read_descriptor(debug=1)
        return dsize

    def start_scan(self):
        self.connection.dtr = False
        self.connection.write(SYNC_BYTE + SCAN_BYTE)
        dsize, none, none = self.read_descriptor(debug=1)
        return dsize

    def get_express(self, dsize):
        bytes_in = self.connection.read(dsize)
        received_sync = (bytes_in[0] & 240) + (bytes_in[1] >> 4)
        if received_sync != ord(SYNC_BYTE):
            raise BufferError("Mismatching Sync bytes")
        else:
            ultra_cabins = []
            start_angle = (bytes_in[2] + ((bytes_in[3] & 127) << 8)) / 64.0
            for i in range(len(bytes_in[4:]) // 5):
                ultra_cabins.append(bytes_in[4 + i * 5: 4 + (i + 1) * 5])

        return ultra_cabins, start_angle

    def parse_scan(self):
        samples = []

        i = 0
        while (self.connection.in_waiting > 5) and (i < MAX_SAMPLES_PER_SCAN):
            bytes_in = self.connection.read(5)
            quality = bytes_in[0] >> 2
            angle = ((bytes_in[1] >> 1) + (bytes_in[2] << 7)) / 64.0
            distance = (bytes_in[3] + (bytes_in[4] << 8)) / 4.0
            samples.append((math.radians(angle), distance))
            i += 1

        return samples

    def get_point_cloud(self, data_size, n_points, max_distance):
        points = []
        while self.connection.in_waiting > data_size:
            self.connection.read(data_size)
        while self.connection.in_waiting < data_size:
            pass
        old_cabins, old_start_angle = self.get_express(data_size)

        while len(points) < n_points:
            while self.connection.in_waiting < data_size:
                pass

            new_cabins, new_start_angle = self.get_express(data_size)
            if new_start_angle >= old_start_angle:
                delta_angle = new_start_angle - old_start_angle
            else:
                delta_angle = new_start_angle + 360.0 - old_start_angle

            samples = parse_cabins(old_cabins, old_start_angle, delta_angle, do_compensation=0)
            old_cabins = new_cabins
            old_start_angle = new_start_angle

            points.extend(get_points(max_distance, samples))
            x = []
            y = []
            for i in range(len(points)):
                x.append(points[i][0])
                y.append(points[i][1])

        return points, x, y
