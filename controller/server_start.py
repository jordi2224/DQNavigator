import socket
import json
from controller.server_tools import *
from controller.GPIOdefinitions import *
import time
from multiprocessing import Process, Pipe

tst_msg = "-----BEGIN TFG MSG-----\ntest\n-----END TFG MSG-----\n"
buff = ""


def control_loop(pipe):
    current_order_t = 0
    max_time_delay = 0.3
    while 1:
        if not pipe.empty():
            msg = pipe.recv()
        else:
            execute(msg)
            current_order_t = time.time()

        if time.time() - current_order_t > max_time_delay:
            halt()


def execute(msg):
    if msg["type"] == "MANUAL_MOVE_ORDER":
        dir = msg["direction"]

        if dir == "FWD":
            forward()
        elif dir == "BWD":
            backwards()
        elif dir == "LEFT":
            forward_right()
            reverse_left()
        elif dir == "RIGHT":
            reverse_right()
            forward_left()
        elif dir == "HALT":
            halt()

    else:
        print("Unknown message")


if __name__ == "__main__":
    server_parent, loop_child = Pipe()
    p = Process(target=control_loop, args=(loop_child,))
    p.start()

    auto_setup()

    TCP_IP = socket.gethostbyname(socket.gethostname())
    TCP_PORT = 420

    BUFFER_SIZE = 64

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)

    conn, addr = s.accept()
    print('Connection address:', addr)
    while 1:
        buff += conn.recv(BUFFER_SIZE).decode('utf-8')

        if is_complete(buff):
            msg, buff = receive_msg(buff)
            msg = parse(msg)
            server_parent.send(msg)

    conn.close()
