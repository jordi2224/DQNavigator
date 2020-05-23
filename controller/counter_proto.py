from controller.GPIOdefinitions import *
import RPi.GPIO as GPIO
import time

previous_state_left = GPIO.input(LTH2)
counter_left = 0

previous_state_right = GPIO.input(RTH2)
counter_right = 0

halt()

while(True):
    new_state_left = GPIO.input(LTH2)
    new_state_right = GPIO.input(RTH2)
    do_output = False

    if new_state_left != previous_state_left:
        if previous_state_left == 0:
             if GPIO.input(LTH1):
                 counter_left -= 1
             else:
                 counter_left += 1
             do_output = True
        previous_state_left = new_state_left

    if new_state_right != previous_state_right:
        if previous_state_right == 0:
            if GPIO.input(RTH1):
                counter_right += 1
            else:
                counter_right -= 1
            do_output = True
        previous_state_right = new_state_right

    if do_output:
        print(counter_left, counter_right)

    time.sleep(0.001)


