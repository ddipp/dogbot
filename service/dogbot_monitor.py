#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

r1, r2 = 17, 18

GPIO.setmode(GPIO.BCM)

GPIO.setup(r1, GPIO.OUT)
GPIO.output(r1, GPIO.LOW)
time.sleep(1)
GPIO.output(r1, GPIO.HIGH)
GPIO.cleanup()
