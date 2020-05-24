import json
import pickle
from controller.GPIOdefinitions import *
import os
import subprocess
import controller.async_movement
from driver.TSFinalDriver import Driver
from controller.comm_definitions import *
from controller.async_counter_proto import *


start_USB_off = False
motor_enable = True

sample_size = 600
max_distance = 5000


def execute(msg, driver, dsize, conn):
    global motor_enable, sample_size, max_distance
    if msg["type"] == "MANUAL_MOVE_ORDER" and motor_enable:
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

    elif msg["type"] == "CONTROLLED_MOVE_ORDER" and motor_enable:
        print(controller.async_movement.execute_move(250, 250));

    elif msg["type"] == "CONFIGURATION":
        device = msg["target"]

        if device == "MOTOR":
            if msg["state"] == 1:
                print("Motor movement enabled by client")
                motor_enable = True
            elif msg["state"] == 0:
                print("Motor movement disabled by client")
                motor_enable = False
            else:
                print('Unexpected value')
        elif device == "USB":
            if msg["state"] == 1:
                os.system('echo \'1-1\' |sudo tee /sys/bus/usb/drivers/usb/bind')
            elif msg["state"] == 0:
                os.system('echo \'1-1\' |sudo tee /sys/bus/usb/drivers/usb/unbind')
            else:
                print('Unexpected value')

        elif device == "PARAMETER":
            if msg["parameter"] == "SAMPLE_SIZE":
                value = msg["value"]
                sample_size = value

            elif msg["parameter"] == "MAX_DISTANCE":
                value = msg["value"]
                max_distance = max_distance
            else:
                print('Unexpected value')

        else:
            print("Unsupported device")

    elif msg["type"] == "REQUEST":
        request = msg["request"]

        if request == "GET_SCAN":
            if driver is not None:
                points, x, y = driver.get_point_cloud(dsize, sample_size, max_distance)

                print("Sending scan data")
                serialized_p = pickle.dumps(points, protocol=0)
                res = START_STR + "{\"type\":\"SCAN_DATA\", \"data_size\": " + str(len(serialized_p)) + " }" + END_STR
                conn.send(res.encode('utf-8'))
                conn.send(DATA_START_STR.encode('utf-8') + serialized_p + DATA_END_STR.encode('utf-8'))

            else:
                res = START_STR + TYPE_STR + "\"ERROR\", \"severity\": 1, \"message\" : \"No driver is running at the " \
                                             "moment, is the LIDAR connected?\"}" + END_STR
                conn.send(res.encode('utf-8'))
                print("Controller attempted to retrieve LIDAR data but to driver is running")

    else:
        print("Unknown message")


def start_driver():
    s = subprocess.check_output(['dmesg'])
    s = s.split(b'\n')
    port = None

    for line in reversed(s):
        if b'cp210x converter now attached to' in line:
            port = line[line.find(b'ttyUSB'):len(line)]
            break

    if not port:
        print("LIDAR is not connected")
        return None, None

    driver = Driver('/dev/' + port.decode('utf-8'))
    dsize = driver.start_scan_express()

    return driver, dsize
