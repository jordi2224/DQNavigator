import pickle
import socket

import numpy as np

from controller.comm_definitions import *


def get_socket(TCP_IP, TCP_PORT):
    """
    Get a TCP socket connection to the desired IP and port
    returns None if this process fails
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        return s
    except:
        return None


def get_def_connection():
    return get_socket('192.168.1.177', 420)


def wait_for_msg(s, buff):
    """
    Halts execution until a full message is available in the TCP buffer
    """
    while not is_complete(buff):
        try:
            buff += s.recv(4096).decode('utf-8')
        except:
            return -1

    return 0, buff


def do_scan(s, buff, sample_size, distance):
    """
        Send a LIDAR scan request to the server
        """
    request = START_STR + str(
        {"type": "REQUEST", "request": "GET_SCAN", "SAMPLE_SIZE": sample_size, "MAX_RANGE": distance}).replace(
        '\'',
        '\"') + END_STR
    s.send(request.encode('utf-8'))

    _, buff = wait_for_msg(s, buff)

    msg = None
    while msg is None:
        _, buff = wait_for_msg(s, buff)
        msg, buff = receive_msg(buff)
        msg = parse(msg)
        if msg["type"] == "SCAN_DATA":
            data_length = msg['data_size']
            while not is_complete(buff) or DATA_END_STR not in buff:
                buff += s.recv(4096).decode('utf-8')

            data, buff = fetch_data(buff, data_length)
            if data is not None:
                points = np.array(pickle.loads(data.encode('utf-8')))
                x = np.transpose(points)[0]
                y = np.transpose(points)[1]
        else:
            msg = None

    return x, y, buff