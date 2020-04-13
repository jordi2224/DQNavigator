import json
import pickle
from controller.GPIOdefinitions import *
import os
import subprocess
from driver.TSFinalDriver import Driver
from controller.comm_definitions import *


start_USB_off = False



def execute(msg, driver, dsize, conn):
    #conn.send("ACK".encode('utf-8'))
    print(msg)
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

    elif msg["type"] == "CONFIGURATION":
        device = msg["device"]

        if device == "USB":
            if msg["state"] == 1:
                os.system('echo \'1-1\' |sudo tee /sys/bus/usb/drivers/usb/bind')
            elif msg["state"] == 0:
                os.system('echo \'1-1\' |sudo tee /sys/bus/usb/drivers/usb/unbind')
            else:
                print('Unexpected value')
        else:
            print("Unsupported device")

    elif msg["type"] == "REQUEST":
        request = msg["request"]

        if request == "GET_SCAN":
            points, x, y = driver.get_point_cloud(dsize, 20, 5000)

            print("Sending scan data")
            serialized_p = pickle.dumps(points, protocol = 0)
            res = START_STR + "{\"type\":\"SCAN_DATA\", \"data_size\": "+ str(len(serialized_p))  +" }" + END_STR
            conn.send(res.encode('utf-8'))
            conn.send(DATA_START_STR.encode('utf-8') + serialized_p + DATA_END_STR.encode('utf-8'))

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
