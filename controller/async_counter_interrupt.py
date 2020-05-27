import RPi.GPIO as GPIO
from controller.GPIOdefinitions import *

counter_L = 0
counter_R = 0


def event_left(sig):
    global counter_L
    if GPIO.input(LTH1):
        if GPIO.input(LTH2):
            counter_L += 1
        else:
            counter_L -= 1
    else:
        if GPIO.input(LTH2):
            counter_L -= 1
        else:
            counter_L += 1


def event_right(sig):
    global counter_R
    if GPIO.input(RTH1):
        if GPIO.input(RTH2):
            counter_R += 1
        else:
            counter_R -= 1
    else:
        if GPIO.input(RTH2):
            counter_R -= 1
        else:
            counter_R += 1


GPIO.add_event_detect(LTH1, GPIO.BOTH, callback=event_left)

GPIO.add_event_detect(RTH1, GPIO.BOTH, callback=event_right)


def get_track_pos():
    return counter_L, counter_R
