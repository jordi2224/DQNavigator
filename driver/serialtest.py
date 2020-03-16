import serial
import time

baudrate = 115200

while(True):
    ser.write(b"hello!\n")
    time.sleep(0.5)

ser.close()