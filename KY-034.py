#!/usr/bin/env python
# -*- coding: utf-8 -*-

import OPi.GPIO as GPIO

import time          # this lets us have a time delay

GPIO.setboard(GPIO.PCPCPLUS)
GPIO.setmode(GPIO.BOARD)

LED_PIN = 16
GPIO.setup(LED_PIN, GPIO.OUT, initial= GPIO.LOW)
  
print ("LED-Test [press ctrl+c to end]")
 
# main program loop
try:
        while True:
                print("LED is on for 4 seconds")
                GPIO.output(LED_PIN,GPIO.HIGH) #LED will be switched on
                time.sleep(4) # Waitmode for 4 seconds
                print("LED is off for 2 seconds") 
                GPIO.output(LED_PIN,GPIO.LOW) #LED will be switched off
                time.sleep(2) # Waitmode for another 2 seconds
   
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
