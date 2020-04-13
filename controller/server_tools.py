import json
import pickle
from controller.GPIOdefinitions import *
import os
import subprocess
from driver.TSFinalDriver import Driver
from controller.comm_definitions import *


start_USB_off = False


def is_complete(buff):
    return START_STR in buff and END_STR in buff


def is_clean(buff):
    return buff[0:len(START_STR)] == START_STR


def clean(buff):
    index = buff.find(START_STR)
    if index > 0:
        return buff[index: len(buff)]
    else:
        return -1


def receive_msg(msg):
    if is_complete(msg):
        if not is_clean(msg):
            print("Buffer is not clean. Some data might have been lost")
            print(msg)
            msg = clean(msg)
            assert msg != -1

        end_index = msg.find(END_STR)
        return msg[len(START_STR): end_index], msg[end_index + len(END_STR): len(msg)]
    else:
        return -1


def parse(buff):
    return json.loads(buff)


def execute(msg, driver, dsize, conn):
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

            serialized_p = pickle.dumps(points)
            msg = START_STR + "{\"type\":\"SCAN_DATA\", \"data\": "+ serialized_p +"}" + END_STR
            conn.send(serialized_p)

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
