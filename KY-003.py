#!/usr/bin/env python
# -*- coding: utf-8 -*-

import orangepi.pc
from OPi import GPIO

from time import sleep          # this lets us have a time delay

GPIO.setmode(GPIO.BOARD)
  
# The input pin of the Sensor will be declared. Additional to that the pullup resistor will be activated.
GPIO_PIN = 26
GPIO.setup(GPIO_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
  
print "Sensor-Test [press ctrl+c to end it]"
  
# This output function will be started at signal detection
def outFunction(null):
        print("Signal detected")
  
# At the moment of detecting a Signal ( falling signal edge ) the output function will be activated.
GPIO.add_event_detect(GPIO_PIN, GPIO.FALLING, callback=outFunction, bouncetime=100) 
  
try:
        while True:
                sleep(1)

except KeyboardInterrupt:  
    # here you put any code you want to run before the program   
    # exits when you press CTRL+C  
    print "An error or exception occurred!"
  
except:  
    # this catches ALL other exceptions including errors.  
    # You won't get any error messages for debugging  
    # so only use it once your code is working  
    print "Other error or exception occurred!"  
  
finally:  
    GPIO.cleanup() # this ensures a clean exit 
