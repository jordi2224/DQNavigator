import socket
import json
from controller.server_tools import *
from controller.GPIOdefinitions import *
import time
from multiprocessing import Process, Pipe, Queue
from driver.TSFinalDriver import Driver

tst_msg = "-----BEGIN TFG MSG-----\ntest\n-----END TFG MSG-----\n"
buff = ""


def control_loop(pipe, driver, dsize, conn):
    print('Control loop started')
    msg = None
    current_order_t = 0
    max_time_delay = 0.1

    channel_active = False
    while 1:
        if not pipe.empty():
            msg = pipe.get()
            channel_active = True
            if msg == "CONN_UPDATE":
                print('Processing connection update')
                conn = pipe.get()
                print("Connection object updated")
                msg = None
        else:
            if msg is not None:
                print(msg)
                execute(msg, driver, dsize, conn)
                current_order_t = time.time()
                msg = None

        if time.time() - current_order_t > max_time_delay and channel_active:
            current_order_t = time.time()
            halt()
            channel_active = False


if __name__ == "__main__":
    if start_USB_off:
        print('Shutting down USB buses to conserve power')
        os.system('echo \'1-1\' |sudo tee /sys/bus/usb/drivers/usb/unbind')

    print("Starting up driver")
    driver, dsize = start_driver()

    if driver:
        print("Expected data size: ", dsize)
    else:
        print("Device not found")

    auto_setup()

    # TCP_IP = socket.gethostbyname(socket.gethostname())
    TCP_IP = '192.168.1.177'
    print(TCP_IP)
    TCP_PORT = 420

    BUFFER_SIZE = 64

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)

    conn, addr = s.accept()

    q = Queue()
    p = Process(target=control_loop, args=(q, driver, dsize, conn,))
    p.start()

    print('Connection address:', addr)
    while 1:
        try:
            buff += conn.recv(BUFFER_SIZE).decode('utf-8')
        except:
            print('Connection to: ', addr, ' was lost, listening at TCP: ', TCP_IP, ':', TCP_PORT)
            s.listen(1)
            conn, addr = s.accept()
            print('Connection address:', addr)
            q.put("CONN_UPDATE")
            q.put(conn)

        if is_complete(buff):
            msg, buff = receive_msg(buff)
            msg = parse(msg)
            q.put(msg)

    conn.close()
