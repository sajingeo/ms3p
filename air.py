#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.OUT)  # Oxygen
GPIO.setup(23,GPIO.OUT)  # Carbondioxide


# fill Oxygen
	GPIO.output(23,True)
	time.sleep(2)
#fill carbondioxide
	GPIO.output(24,True)
	time.sleep(2)
# fill complete
	GPIO.output(23,False)
	GPIO.output(24,False)