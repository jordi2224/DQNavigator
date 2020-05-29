import RPi.GPIO as GPIO
from controller.GPIOdefinitions import *
from multiprocessing import Process, Value

counter_L = Value('q')
counter_R = Value('q')

rotational_calibration = 196.0
linear_calibration = 1.0

def event_left(sig):
    if GPIO.input(LTH1):
        if GPIO.input(LTH2):
            counter_L.value -= 1
        else:
            counter_L.value += 1
    else:
        if GPIO.input(LTH2):
            counter_L.value += 1
        else:
            counter_L.value -= 1


def event_right(sig):
    global counter_R
    if GPIO.input(RTH1):
        if GPIO.input(RTH2):
            counter_R.value += 1
        else:
            counter_R.value -= 1
    else:
        if GPIO.input(RTH2):
            counter_R.value -= 1
        else:
            counter_R.value += 1


def get_track_pos():
    return counter_L.value, counter_R.value


def setup():
    GPIO.add_event_detect(LTH1, GPIO.BOTH, callback=event_left)
    GPIO.add_event_detect(RTH1, GPIO.BOTH, callback=event_right)
    print("Tracking events setup")
    while True:
        time.sleep(10)
        print(get_track_pos())


track_position_process = Process(target=setup, )
track_position_process.start()
