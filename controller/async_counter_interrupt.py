import RPi.GPIO as GPIO
from controller.GPIOdefinitions import *
from multiprocessing import Process, Value

counter_L = Value('q')
counter_R = Value('q')

halt_target_flag = Value('b')
halt_target_secondary_flag_L = Value('b')
halt_target_secondary_flag_R = Value('b')

halt_target_L = Value('q')
halt_target_R = Value('q')

rotational_calibration = 212.0
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

    if halt_target_flag.value:
        if counter_L == halt_target_L:
            halt_left()
            halt_target_secondary_flag_L.value = 1
            if halt_target_secondary_flag_R.value:
                halt()
                halt_target_flag.value = 0
                halt_target_secondary_flag_L.value = 0
                halt_target_secondary_flag_R.value = 0


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
    if halt_target_flag.value:
        if counter_R == halt_target_R:
            halt_left()
            halt_target_secondary_flag_R.value = 1
            if halt_target_secondary_flag_L.value:
                halt()
                halt_target_flag.value = 0
                halt_target_secondary_flag_L.value = 0
                halt_target_secondary_flag_R.value = 0


def get_track_pos():
    return counter_L.value, counter_R.value


def setup():
    halt_target_flag.value = 0
    halt_target_secondary_flag_L.value = 0
    halt_target_secondary_flag_R.value = 0
    GPIO.add_event_detect(LTH1, GPIO.BOTH, callback=event_left)
    GPIO.add_event_detect(RTH1, GPIO.BOTH, callback=event_right)
    print("Tracking events setup")


def set_halt_target(target_L, target_R):
    halt_target_flag.value = 1
    halt_target_secondary_flag_L.value = 0
    halt_target_secondary_flag_R.value = 0
    halt_target_L.value = target_L
    halt_target_R.value = target_R


track_position_process = Process(target=setup, )
track_position_process.start()
