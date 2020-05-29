import pickle
import socket

import numpy as np

from controller.comm_definitions import *

# PSEUDO CODE


# MAIN
from preprocessing.wallsCV import doHoughTransform

TCP_IP = '192.168.1.177'
TCP_PORT = 420


def get_socket(TCP_IP, TCP_PORT):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        return s
    except:
        return None


def wait_for_msg(s, buff):
    while not is_complete(buff):
        try:
            buff += s.recv(4096).decode('utf-8')
        except:
            return -1

    return 0, buff


def request_scan(s):
    request = START_STR + str({"type": "REQUEST", "request": "GET_SCAN"}).replace('\'', '\"') + END_STR
    s.send(request.encode('utf-8'))


def receive_scan(s, buff):
    msg = None
    while msg is None:
        _, buff = wait_for_msg(s, buff)
        msg, buff = receive_msg(buff)
        msg = parse(msg)
        if msg["type"] == "SCAN_DATA":
            data_length = msg['data_size']
            while not is_complete(buff):
                buff += s.recv(4096).decode('utf-8')
            data, buff = fetch_data(buff, data_length)
            if data is not None:
                points = np.array(pickle.loads(data.encode('utf-8')))
                x = np.transpose(points)[0]
                y = np.transpose(points)[1]
        else:
            msg = None

    return x, y


def receive_rotation_report(s, buff):
    msg = None
    while msg is None:
        _, buff = wait_for_msg(s, buff)
        msg = parse(msg)
        if msg["type"] == "MOVEMENT_ORDER_REPORT":
            old_theta = msg["initial_theta"]
            new_theta = msg["current_theta"]
            return old_theta, new_theta
        else:
            msg = None
    return None, None


if __name__ == "__main__":

    # Establishing a connection to drone's TCP server
    s = get_socket(TCP_IP, TCP_PORT)
    buff = ''

    # Scan request / Scan process
    request_scan(s)
    x, y = receive_scan(s, buff)

    # Find walls
    initial_walls, offset_x, offset_y = doHoughTransform(x, y, 8)

    for wall in initial_walls:
        print(wall.rho, wall.theta)

    rotation_message = START_STR + str({"type": "CONTROLLED_MOVE_ORDER", "movement": "ROTATION", "value": 340}).replace('\'', '\"') + END_STR
    s.send(rotation_message.encode('utf-8'))

    old_theta, new_theta = receive_rotation_report(s, buff)
    delta_theta = new_theta - old_theta
    print("\n\nDelta theta: ", delta_theta)
    print("\n\n")
    # New scan!
    request_scan(s)
    x, y = receive_scan(s, buff)

    # Find walls
    new_walls, offset_x, offset_y = doHoughTransform(x, y, 8)
    for wall in initial_walls:
        print(wall.rho, wall.theta)
# FIND THE WALLS IN THIS NEW SCAN

# COMPARE TO EXPECTED POSITION OF WALLS

# FIND IF WALLS SEEM TO MATCH (COMPARE ANGULAR DISTANCES OF WALLS SIMILARLY FAR??)

# EXECUTE ANOTHER CONTROLLED MOVE ORDER TO ATTEMPT TO CORRECT THIS

# JUMP TO LOOP