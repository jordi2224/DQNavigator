import RPi.GPIO as GPIO
import time

# TODO: Remove this
# This is a test test test

RT_F = 12
RT_R = 33
RTH1 = 38
RTH2 = 40

LT_F = 36
LT_R = 11
LTH1 = 15
LTH2 = 7

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
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(RT_F, GPIO.OUT)
    GPIO.setup(RT_R, GPIO.OUT)
    GPIO.setup(LT_R, GPIO.OUT)
    GPIO.setup(LT_F, GPIO.OUT)


def halt():
    GPIO.output(RT_F, 0)
    GPIO.output(RT_R, 0)
    GPIO.output(LT_F, 0)
    GPIO.output(LT_R, 0)


def forward_left():
    GPIO.output(LT_R, 0)
    GPIO.output(LT_F, 1)


def reverse_left():
    GPIO.output(LT_F, 0)
    GPIO.output(LT_R, 1)


def forward_right():
    GPIO.output(RT_R, 0)
    GPIO.output(RT_F, 1)


def reverse_right():
    GPIO.output(RT_F, 0)
    GPIO.output(RT_R, 1)


def forward():
    forward_right()
    forward_left()


def backwards():
    reverse_right()
    reverse_left()


def fl1s():
    forward_left()
    time.sleep(1)
    halt()


def fr1s():
    forward_right()
    time.sleep(1)
    halt()


def f1s():
    forward_right()
    forward_left()
    time.sleep(1)
    halt()
