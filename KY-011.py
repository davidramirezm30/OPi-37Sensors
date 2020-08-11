#!/usr/bin/env python
# -*- coding: utf-8 -*-

import OPi.GPIO as GPIO

import random
from time import sleep          # this lets us have a time delay

GPIO.setboard(GPIO.PCPCPLUS)
GPIO.setmode(GPIO.BOARD)

# The output pins will be declared, which are connected with the LEDs. 
LED_Red = 18
LED_Green = 16
# Set pins to output mode
GPIO.setup(LED_Red, GPIO.OUT, initial= GPIO.LOW)
GPIO.setup(LED_Green, GPIO.OUT, initial= GPIO.LOW)
  
print "LED-Test [press ctrl+c to end]"
  
# main program loop
try:
        while True:
            print("LED Red is on for 3 seconds")
            GPIO.output(LED_Green,GPIO.HIGH) #LED will be switched on
            GPIO.output(LED_Red,GPIO.LOW) #LED will be switched off
            sleep(3) # Waitmode for 3 seconds
            print("LED Green is on for 3 seconds") 
            GPIO.output(LED_Green,GPIO.LOW) #LED will be switched off
            GPIO.output(LED_Red,GPIO.HIGH) #LED will be switched on
            sleep(3) #Waitmode for 3 seconds

  
except:  
    # this catches ALL other exceptions including errors.  
    # You won't get any error messages for debugging  
    # so only use it once your code is working  
    print ("Other error or exception occurred!")
  
finally:  
    GPIO.cleanup() # this ensures a clean exit 