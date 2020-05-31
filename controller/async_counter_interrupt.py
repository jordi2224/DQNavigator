from multiprocessing import Value

import RPi.GPIO as GPIO

from controller.GPIOdefinitions import *

"""
Interrupt base track position tracking
Allows for asynchronous counting of pulses from rotary encoders
Uses interrupts triggered by GPIO pin status changes
Can also trigger a halt at particular counts
"""

# Shared variables with tracking threads
# Should not be read directly; use get_track_pos() instead

# Counters
counter_L = Value('q')
counter_R = Value('q')

# Flags
halt_target_flag = Value('b')
halt_target_secondary_flag_L = Value('b')
halt_target_secondary_flag_R = Value('b')
# Halt targets
halt_target_L = Value('q')
halt_target_R = Value('q')

# Pulses per radian
rotational_calibration = 212.0
# Pulses per millimeter TODO
linear_calibration = 1.0


# Function triggered by left encoder edge
def event_left(sig):
    global counter_L

    # Rising edge of LTH1
    if GPIO.input(LTH1):
        # Uses LTH2 to determine direction
        if GPIO.input(LTH2):
            counter_L.value -= 1
        else:
            counter_L.value += 1
    # Falling edge of LTH1
    else:
        # Uses LTH2 to determine direction
        if GPIO.input(LTH2):
            counter_L.value += 1
        else:
            counter_L.value -= 1

    # Check if halting flag has been set
    if halt_target_flag.value:
        # If a halting target has been set check if we have reached it
        if counter_L == halt_target_L:

            # Halt this track and set corresponding flag
            halt_left()
            halt_target_secondary_flag_L.value = 1

            # Check if the other target was also reached
            if halt_target_secondary_flag_R.value:
                # Halt both tracks and clear flags; we are done
                halt()
                halt_target_flag.value = 0
                halt_target_secondary_flag_L.value = 0
                halt_target_secondary_flag_R.value = 0


def event_right(sig):
    global counter_R

    # Rising edge of RTH1
    if GPIO.input(RTH1):
        # Uses RTH2 to determine direction
        if GPIO.input(RTH2):
            counter_R.value += 1
        else:
            counter_R.value -= 1
    # Falling edge of RTH1
    else:
        # Uses RTH2 to determine direction
        if GPIO.input(RTH2):
            counter_R.value -= 1
        else:
            counter_R.value += 1

    # Check if halting flag has been set
    if halt_target_flag.value:
        # If a halting target has been set check if we have reached it
        if counter_R == halt_target_R:

            # Halt this track and set corresponding flag
            halt_left()
            halt_target_secondary_flag_R.value = 1

            # Check if the other target was also reached
            if halt_target_secondary_flag_L.value:
                # Halt both tracks and clear flags; we are done
                halt()
                halt_target_flag.value = 0
                halt_target_secondary_flag_L.value = 0
                halt_target_secondary_flag_R.value = 0


def get_track_pos():
    """Returns the current position of tracks"""
    return counter_L.value, counter_R.value


def setup():
    """
    Setups the interrupts for position tracking
    Running it again at any point would clear the flags for halting targets
    Greatly discourage running again
    """
    halt_target_flag.value = 0
    halt_target_secondary_flag_L.value = 0
    halt_target_secondary_flag_R.value = 0
    GPIO.add_event_detect(LTH1, GPIO.BOTH, callback=event_left)
    GPIO.add_event_detect(RTH1, GPIO.BOTH, callback=event_right)
    print("Tracking events setup")


def set_halt_target(target_L, target_R):
    """
    Set a halt target for interrupts
    Interrupt functions will attempt to call a halt maneuver whenever target_L/R has been reached
    This slows down the interrupt function; might cause missed steps potentially
    """
    halt_target_flag.value = 1
    halt_target_secondary_flag_L.value = 0
    halt_target_secondary_flag_R.value = 0
    halt_target_L.value = int(target_L)
    halt_target_R.value = int(target_R)
