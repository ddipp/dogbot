#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

r1, r2 = 17, 18
b1 = 23

GPIO.setmode(GPIO.BCM)

GPIO.setup(b1, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:

    buttonState = GPIO.input(b1)
    print('b1 = ' buttonState)

    GPIO.setup(r1, GPIO.OUT)
    GPIO.output(r1, GPIO.LOW)
    time.sleep(1)
    GPIO.output(r1, GPIO.HIGH)

    GPIO.setup(r2, GPIO.OUT)
    GPIO.output(r2, GPIO.LOW)
    time.sleep(1)
    GPIO.output(r2, GPIO.HIGH)

GPIO.cleanup()
