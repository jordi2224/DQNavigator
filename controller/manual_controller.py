import socket
import keyboard
import time

TCP_IP = '192.168.1.177'
TCP_PORT = 420


if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))

    while 1:
        if keyboard.is_pressed('w') and not keyboard.is_pressed('s') and not keyboard.is_pressed('a') and not keyboard.is_pressed('d'):
            msg = "-----BEGIN TFG MSG-----\n{\"type\":\"MANUAL_MOVE_ORDER\", \"direction\": \"FWD\"}\n-----END TFG " \
                  "MSG-----\n"
            s.send(msg.encode('utf-8'))
        elif not keyboard.is_pressed('w') and keyboard.is_pressed('s') and not keyboard.is_pressed('a') and not keyboard.is_pressed('d'):
            msg = "-----BEGIN TFG MSG-----\n{\"type\":\"MANUAL_MOVE_ORDER\", \"direction\": \"BWD\"}\n-----END TFG " \
                  "MSG-----\n"
            s.send(msg.encode('utf-8'))
        elif not keyboard.is_pressed('w') and not keyboard.is_pressed('s') and keyboard.is_pressed('a') and not keyboard.is_pressed('d'):
            msg = "-----BEGIN TFG MSG-----\n{\"type\":\"MANUAL_MOVE_ORDER\", \"direction\": \"RIGHT\"}\n-----END TFG " \
                  "MSG-----\n"
            s.send(msg.encode('utf-8'))
        elif not keyboard.is_pressed('w') and not keyboard.is_pressed('s') and not keyboard.is_pressed('a') and keyboard.is_pressed('d'):
            msg = "-----BEGIN TFG MSG-----\n{\"type\":\"MANUAL_MOVE_ORDER\", \"direction\": \"LEFT\"}\n-----END TFG " \
                  "MSG-----\n"
            s.send(msg.encode('utf-8'))

        time.sleep(0.1)