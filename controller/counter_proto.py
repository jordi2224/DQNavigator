from controller.GPIOdefinitions import *
import RPi.GPIO as GPIO
import time

LH2 = 40

GPIO.setup(LH2, GPIO.IN)

previous_state = GPIO.input(LH2)
counter = 0

while(True):
    new_state = GPIO.input(LH2)
    if new_state != previous_state:
        if previous_state == 0:
             counter += 1
             print(counter)
        previous_state = new_state

    time.sleep(0.001)



