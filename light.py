#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT)  # Lights
# this would a deactivate command would kill this process and reset the pins


# fill Oxygen
	GPIO.output(23,True)
	
# 