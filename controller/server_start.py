import socket
from controller.server_tools import *
from controller.GPIOdefinitions import *
import time
from multiprocessing import Process, Queue


def control_loop(queue, driver_object, lidar_data_size, connection_object):
    # Control loop
    # This loop is meant to be executed in a different process from the TCP server
    # Receives, validates and executes messages coming from the queue object
    #
    # Input parameters:
    # queue: multiprocessing.Queue object. Only expected to read, not write
    # driver_object: LIDAR driver object. Can be None if LIDAR is not plugged in or somehow unavailable
    # lidar_data_size: size of data that the driver expects from sensor, to be removes in future versions TODO
    # connection_object: connection object with controller. Needed to send replies.
    # DO NOT READ FROM IT OTHERWISE INPUT BUFFER MIGHT GET CORRUPTED!!!

    print('Control loop started')
    message = None
    # Time at which the last order was executed
    current_manual_order_t = 0
    # Maximum delay between orders before the channel is considered inactive, at this time control loop will attempt a
    # safe halt (aka not interrupt long or scheduled executions)
    max_time_delay = 0.2
    enable_auto_halting = False

    last_exec = None
    while True:
        # All messages are read but only the last one is executed
        # Since most order executions are asynchronous an order being stale and not executed is very unlikely
        if not queue.empty():
            message = queue.get()

            # If message is a connection update precursor update the current connection object
            if message == "CONN_UPDATE":
                print('Processing connection update')
                connection_object = queue.get()
                print("Connection object updated")
                # No order is executed here, just the update
                message = None

        # Only execute messages if no other messages are available in queue
        else:  # Command execution
            if message is not None:
                print(message)
                # Send to execution function
                execute(message, driver_object, lidar_data_size, connection_object)
                if message["type"] == "MANUAL_MOVE_ORDER":
                    current_manual_order_t = time.time()
                    enable_auto_halting = True
                message = None

        if time.time() - current_manual_order_t > max_time_delay and enable_auto_halting:
            halt()
            enable_auto_halting = False


if __name__ == "__main__":
    # Main server loop
    # Maintains a TCP server on 192.168.1.177:420
    # Feed incoming messages to control loop

    # Check configuration to determine initial USB power status
    if start_USB_off:
        print('Shutting down USB buses to conserve power')
        os.system('echo \'1-1\' |sudo tee /sys/bus/usb/drivers/usb/unbind')

    # Attempt to start the LIDAR driver
    print("Starting up driver")
    driver, dsize = start_driver()
    # If the LIDAR is not plugged in, scanning features are unavailable until driver is restarted
    if driver:
        print("Expected data size: ", dsize)
    else:
        print("Device not found")

    # Setup GPIO pins
    auto_setup()

    # Start the TCP server and wait for first connection
    TCP_IP = '192.168.1.177'
    print(TCP_IP)
    TCP_PORT = 420
    BUFFER_SIZE = 64

    # Bind so socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)
    buff = ""

    conn, address = s.accept()

    # Start a subprocess for message execution and open a pipe queue
    # Queue q is used to send messages to control loop
    # Messages are validated by server loop for headers and footers but not for format
    q = Queue()
    p = Process(target=control_loop, args=(q, driver, dsize, conn,))
    p.start()

    print('Connection address:', address)
    while True:
        # If the connection becomes unavailable we try to accept a new one
        try:
            buff += conn.recv(BUFFER_SIZE).decode('utf-8')
        except:
            # Get the new connection and notify control loop
            # Control loop needs the new connection object to reply to requests from the controller

            print('Connection to: ', address, ' was lost, listening at TCP: ', TCP_IP, ':', TCP_PORT)
            s.listen(1)
            conn, address = s.accept()
            print('Connection address:', address)
            q.put("CONN_UPDATE")
            q.put(conn)

        # Check whether a complete message is available for execution
        # This is done by checking if a header and footer are both available in the buffer
        if is_complete(buff):
            # Parse and send the message to control loop
            msg, buff = receive_msg(buff)
            msg = parse(msg)
            if msg["type"] == "FORCE_DISCONNECT":
                conn.close()
            else:
                q.put(msg)

    # Unreachable except by interrupting the server loop
    conn.close()
