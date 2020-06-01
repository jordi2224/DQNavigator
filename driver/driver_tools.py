import math

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

HEALTH_STATUSES = {
    0: 'Good',
    1: 'Warning',
    2: 'Error',
}

STOP_BYTE = b'\x25'

angle_offset = 10


def prepare_payload(cmd_type, payload):
    checksum = 0
    checksum = checksum ^ ord(SYNC_BYTE)
    checksum = checksum ^ ord(cmd_type)
    checksum = checksum ^ len(payload)
    for byte in payload:
        checksum = checksum ^ byte

    return bytes(SYNC_BYTE) + cmd_type + bytes([len(payload)]) + payload + bytes([checksum])


def parse_cabins(cabins, start_angle, delta_angle, do_compensation=0):
    angle = start_angle
    points = []
    for cabin in cabins:
        distance1 = ((cabin[0] >> 2) + (cabin[1] << 6))
        distance2 = ((cabin[2] >> 2) + (cabin[3] << 6))
        dt1 = ((cabin[4] & 15) + ((cabin[0] & 3) << 4))
        dt2 = (((cabin[4] & 240) >> 4) + ((cabin[2] & 3) << 4))

        if do_compensation:
            if dt1 >> 5:
                dt1 = -(dt1 & 31)
            else:
                dt1 = (dt1 & 31)
            if dt2 >> 5:
                dt2 = -(dt1 & 31)
            else:
                dt2 = (dt2 & 31)

            angle += delta_angle / 32.0
            points.append((math.radians((angle + dt1 / 32.0) % 360.0), distance1))
            angle += delta_angle / 32.0
            points.append((math.radians((angle + dt2 / 32.0) % 360.0), distance2))
        else:
            angle += delta_angle / 32.0
            points.append((math.radians(angle % 360.0), distance1))
            angle += delta_angle / 32.0
            points.append((math.radians(angle % 360.0), distance2))

    return points


def get_points(max_distance, samples):
    points = []
    for i in range(len(samples)):
        sample = samples[i]
        if sample[1] < max_distance and sample[1] != 0.0:
            y = (math.cos(sample[0] + angle_offset) * sample[1])
            x = (math.sin(sample[0] + angle_offset) * sample[1])

            points.append((x, y))
    return points
