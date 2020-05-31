import RPi.GPIO as GPIO

"""
Definitions and functions for using the RPi's GPIOs
Using miss-timing in H-bridge control pins will cause damage to bridge, motors and/or RPi
Some of this function should never ever be called asynchronously
"""

# Right track pins
RT_F = 12
RT_R = 35
RTH1 = 38
RTH2 = 40

# Left track pins
LT_F = 36
LT_R = 11
LTH1 = 15
LTH2 = 7

# Setup pins according to use
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(RT_F, GPIO.OUT)
GPIO.setup(RT_R, GPIO.OUT)
GPIO.setup(LT_R, GPIO.OUT)
GPIO.setup(LT_F, GPIO.OUT)
GPIO.setup(RTH1, GPIO.IN)
GPIO.setup(RTH2, GPIO.IN)
GPIO.setup(LTH1, GPIO.IN)
GPIO.setup(LTH2, GPIO.IN)


def auto_setup():
    """Repeat setup in case it's necessary"""
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(RT_F, GPIO.OUT)
    GPIO.setup(RT_R, GPIO.OUT)
    GPIO.setup(LT_R, GPIO.OUT)
    GPIO.setup(LT_F, GPIO.OUT)
    GPIO.setup(RTH1, GPIO.IN)
    GPIO.setup(RTH2, GPIO.IN)
    GPIO.setup(LTH1, GPIO.IN)
    GPIO.setup(LTH2, GPIO.IN)


def halt_left():
    """Halt the left track"""
    GPIO.output(LT_F, 0)
    GPIO.output(LT_R, 0)


def halt_right():
    """Halt the right track"""
    GPIO.output(RT_F, 0)
    GPIO.output(RT_R, 0)


def halt(quiet=False):
    """Halt both track, use argument quiet=True to suppress debug message"""
    GPIO.output(RT_F, 0)
    GPIO.output(RT_R, 0)
    GPIO.output(LT_F, 0)
    GPIO.output(LT_R, 0)
    if not quiet:
        print("Someone called a TOTAL halt")


def forward_left():
    """Move left track forwards"""
    """NEVER CALL ASYNCHRONOUSLY"""
    GPIO.output(LT_R, 0)
    GPIO.output(LT_F, 1)


def reverse_left():
    """Move left track backwards"""
    """NEVER CALL ASYNCHRONOUSLY"""
    GPIO.output(LT_F, 0)
    GPIO.output(LT_R, 1)


def forward_right():
    """Move right track forwards"""
    """NEVER CALL ASYNCHRONOUSLY"""
    GPIO.output(RT_R, 0)
    GPIO.output(RT_F, 1)


def reverse_right():
    """Move right track backwards"""
    """NEVER CALL ASYNCHRONOUSLY"""
    GPIO.output(RT_F, 0)
    GPIO.output(RT_R, 1)


def forward():
    """Move both tracks forwards"""
    """NEVER CALL ASYNCHRONOUSLY"""
    forward_right()
    forward_left()


def backwards():
    """Move both tracks backwards"""
    """NEVER CALL ASYNCHRONOUSLY"""
    reverse_right()
    reverse_left()
