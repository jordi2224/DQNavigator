import pickle
import socket
import keyboard
import time
from controller.comm_definitions import *
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.gca()
max_distance = 1000
plt.axis([-max_distance, max_distance, -max_distance, max_distance])


TCP_IP = '192.168.1.177'
TCP_PORT = 420

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    request = START_STR + "{\"type\":\"REQUEST\", \"request\": \"GET_SCAN\"}" + END_STR
    s.send(request.encode('utf-8'))
    s.settimeout(0.01)
    buff = ''

    counter = 0
    while 1:
        try:
            buff += s.recv(4096).decode('utf-8')
        except:
            pass
        counter += 1

        if not counter % 50:
            counter = 0
            s.send(request.encode('utf-8'))
            print("Requested data")

        if is_complete(buff):
            msg, buff = receive_msg(buff)
            msg = parse(msg)
            if msg['type'] == "SCAN_DATA":
                data_length = msg['data_size']

                data, buff = fetch_data(buff, data_length)
                points = np.array(pickle.loads(data.encode('utf-8')))
                x = np.transpose(points)[0]
                y = np.transpose(points)[1]
                print(x)
                ax.scatter(x, y, s=1)

                ax.set_aspect('equal')
                plt.ioff()
                plt.show()

        if keyboard.is_pressed('w') and not keyboard.is_pressed('s') and not keyboard.is_pressed(
                'a') and not keyboard.is_pressed('d'):
            msg = START_STR + "{\"type\":\"MANUAL_MOVE_ORDER\", \"direction\": \"FWD\"}" + END_STR
            s.send(msg.encode('utf-8'))
        elif not keyboard.is_pressed('w') and keyboard.is_pressed('s') and not keyboard.is_pressed(
                'a') and not keyboard.is_pressed('d'):
            msg = START_STR + "{\"type\":\"MANUAL_MOVE_ORDER\", \"direction\": \"BWD\"}" + END_STR
            s.send(msg.encode('utf-8'))
        elif not keyboard.is_pressed('w') and not keyboard.is_pressed('s') and keyboard.is_pressed(
                'a') and not keyboard.is_pressed('d'):
            msg = START_STR + "{\"type\":\"MANUAL_MOVE_ORDER\", \"direction\": \"RIGHT\"}" + END_STR
            s.send(msg.encode('utf-8'))
        elif not keyboard.is_pressed('w') and not keyboard.is_pressed('s') and not keyboard.is_pressed(
                'a') and keyboard.is_pressed('d'):
            msg = START_STR + "{\"type\":\"MANUAL_MOVE_ORDER\", \"direction\": \"LEFT\"}" + END_STR
            s.send(msg.encode('utf-8'))

        if keyboard.is_pressed('f'):
            msg = {"type": "CONTROLLED_MOVE_ORDER", "dir" : "FWD", "value": 250}
            msg = START_STR + str(msg).replace('\'', '\"') + END_STR
            s.send(msg.encode('utf-8'))

        time.sleep(0.1)
