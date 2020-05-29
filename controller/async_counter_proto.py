import time
import RPi.GPIO as GPIO
from controller.GPIOdefinitions import *
from multiprocessing import Process, Value
from controller._private_decorators import *

counter_L = Value('q')
counter_R = Value('q')


@deprecated
def counter_loop():
    previous_state_left = GPIO.input(LTH2)
    previous_state_right = GPIO.input(RTH2)

    while True:
        new_state_left = GPIO.input(LTH2)
        new_state_right = GPIO.input(RTH2)

        if new_state_left != previous_state_left:
            if previous_state_left == 0:
                if GPIO.input(LTH1):
                    counter_L.value += 1
                else:
                    counter_L.value -= 1
            else:
                if GPIO.input(LTH1):
                    counter_L.value -= 1
                else:
                    counter_L.value += 1

            previous_state_left = new_state_left

        if new_state_right != previous_state_right:
            if previous_state_right == 0:
                if GPIO.input(RTH1):
                    counter_R.value -= 1
                else:
                    counter_R.value += 1
            else:
                if GPIO.input(RTH1):
                    counter_R.value += 1
                else:
                    counter_R.value -= 1

            previous_state_right = new_state_right

        time.sleep(0.001)


track_position_process = Process(target=counter_loop, )
track_position_process.start()


@deprecated
def get_track_pos():
    return counter_L.value, counter_R.value
