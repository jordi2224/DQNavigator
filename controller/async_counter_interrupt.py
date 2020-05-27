import RPi.GPIO as GPIO
from controller.GPIOdefinitions import *

counter_L = 0
counter_R = 0


def event_left_rising(sig):
    global counter_L
    if GPIO.input(LTH2):
        counter_L += 1
    else:
        counter_L -= 1


def event_left_falling(sig):
    global counter_L
    if GPIO.input(LTH2):
        counter_L -= 1
    else:
        counter_L += 1


def event_right_rising(sig):
    global counter_R
    if GPIO.input(RTH2):
        counter_R += 1
    else:
        counter_R -= 1


def event_right_falling(sig):
    global counter_R
    if GPIO.input(RTH2):
        counter_R -= 1
    else:
        counter_R += 1


GPIO.add_event_detect(LTH1, GPIO.RISING, callback=event_left_rising)
GPIO.add_event_detect(LTH1, GPIO.FALLING, callback=event_left_falling)

GPIO.add_event_detect(RTH1, GPIO.RISING, callback=event_right_rising)
GPIO.add_event_detect(RTH1, GPIO.FALLING, callback=event_right_falling)


def get_track_pos():
    return counter_L, counter_R
