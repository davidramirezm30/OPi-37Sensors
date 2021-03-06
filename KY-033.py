#!/usr/bin/env python
# -*- coding: utf-8 -*-

import OPi.GPIO as GPIO

import time          # this lets us have a time delay

GPIO.setboard(GPIO.PCPCPLUS)
GPIO.setmode(GPIO.BOARD)

# Declaration of the input pin which is connected with the sensor.
GPIO_PIN = 7
GPIO.setup(GPIO_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
 
# Break between the results will be defined here (in seconds)
delayTime = 0.5
 
print ("Sensor-test [press ctrl+c to end]")
 
# main program loop
try:
        while True:
            if GPIO.input(GPIO_PIN) == True:
                print ("LineTracker is on the line")
            else:
                print ("Linetracker is not on the line")
            print ("---------------------------------------")
 
            # Reset + Delay
            time.sleep(delayTime)
   
# Scavenging work after the end of the program
except KeyboardInterrupt:  
    # here you put any code you want to run before the program   
    # exits when you press CTRL+C  
    print ("An error or exception occurred!")
  
except:  
    # this catches ALL other exceptions including errors.  
    # You won't get any error messages for debugging  
    # so only use it once your code is working  
    print ("Other error or exception occurred!")
  
finally:  
    GPIO.cleanup() # this ensures a clean exit 
