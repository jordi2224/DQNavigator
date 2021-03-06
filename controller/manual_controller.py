import pickle
import socket
import time

import keyboard
import matplotlib.pyplot as plt
import numpy as np

from controller.comm_definitions import *

fig = plt.figure()
ax = fig.gca()
max_distance = 1000
plt.axis([-max_distance, max_distance, -max_distance, max_distance])

TCP_IP = '192.168.1.177'
TCP_PORT = 420

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    buff = ''
    request = START_STR + str({"type": "REQUEST", "request": "GET_SCAN", "SAMPLE_SIZE": 5000, "MAX_RANGE": 5000}).replace('\'', '\"') + END_STR
    s.send(request.encode('utf-8'))
    s.settimeout(0.1)

    counter = 0
    while 1:
        try:
            buff += s.recv(4096).decode('utf-8')
        except:
            pass
        counter += 1

        if counter == 15:
            counter = 0
            s.send(request.encode('utf-8'))
            print("Requested data")

        if is_complete(buff):
            msg, buff = receive_msg(buff)
            msg = parse(msg)
            if msg['type'] == "SCAN_DATA":
                data_length = msg['data_size']

                while not is_complete(buff):
                    buff += s.recv(4096).decode('utf-8')
                data, buff = fetch_data(buff, data_length)
                if data is not None:
                    points = np.array(pickle.loads(data.encode('utf-8')))
                    x = np.transpose(points)[0]
                    y = np.transpose(points)[1]
                    plt.clf()
                    ax = fig.gca()
                    plt.axis([-max_distance, max_distance, -max_distance, max_distance])
                    ax.scatter(x, y, s=1)

                    ax.set_aspect('equal')
                    ax.set_yticklabels([])
                    ax.set_xticklabels([])
                    ax.grid(True, which='both')
                    ax.axhline(y=0, color='k')
                    ax.axvline(x=0, color='k')

                    plt.ion()
                    plt.show()
                    plt.pause(0.01)

        msg = {"type": "None"}

        if keyboard.is_pressed('w') and not keyboard.is_pressed('s') and not keyboard.is_pressed(
                'a') and not keyboard.is_pressed('d'):
            msg["type"] = "MANUAL_MOVE_ORDER"
            msg["direction"] = "FWD"

        elif not keyboard.is_pressed('w') and keyboard.is_pressed('s') and not keyboard.is_pressed(
                'a') and not keyboard.is_pressed('d'):
            msg["type"] = "MANUAL_MOVE_ORDER"
            msg["direction"] = "BWD"

        elif not keyboard.is_pressed('w') and not keyboard.is_pressed('s') and keyboard.is_pressed(
                'a') and not keyboard.is_pressed('d'):
            msg["type"] = "MANUAL_MOVE_ORDER"
            msg["direction"] = "LEFT"

        elif not keyboard.is_pressed('w') and not keyboard.is_pressed('s') and not keyboard.is_pressed(
                'a') and keyboard.is_pressed('d'):
            msg["type"] = "MANUAL_MOVE_ORDER"
            msg["direction"] = "RIGHT"

        x = 350
        if keyboard.is_pressed('i'):
            msg = {"type": "CONTROLLED_MOVE_ORDER", "movement": "LINEAR", "value": x}
        elif keyboard.is_pressed('k'):
            msg = {"type": "CONTROLLED_MOVE_ORDER", "movement": "LINEAR", "value": -x}
        elif keyboard.is_pressed('l'):
            msg = {"type": "CONTROLLED_MOVE_ORDER", "movement": "ROTATION", "value": -x}
        elif keyboard.is_pressed('j'):
            msg = {"type": "CONTROLLED_MOVE_ORDER", "movement": "ROTATION", "value": x}

        if keyboard.is_pressed('h'):
            msg = {"type": "HALT_OVERRIDE"}

        if msg["type"] != "None":
            msg = START_STR + str(msg).replace('\'', '\"') + END_STR
            s.send(msg.encode('utf-8'))
            print('.', end='')

        time.sleep(0.05)