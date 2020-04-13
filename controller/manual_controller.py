import socket
import keyboard
import time
from controller.comm_definitions import *

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
            print(msg)



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

        time.sleep(0.1)
