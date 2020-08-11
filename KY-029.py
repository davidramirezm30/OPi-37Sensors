#!/usr/bin/env python
# -*- coding: utf-8 -*-

import OPi.GPIO as GPIO

import random
from time import sleep          # this lets us have a time delay

GPIO.setboard(GPIO.PCPCPLUS)
GPIO.setmode(GPIO.BOARD)

# The output pins will be declared, which are connected with the LEDs. 
LED_Red = 16
LED_Green = 18
# Set pins to output mode
GPIO.setup(LED_Red, GPIO.OUT) 
GPIO.setup(LED_Green, GPIO.OUT)
  
Freq = 100 #Hz
  
# The specific colors will be initialized.
RED = GPIO.PWM(LED_Red, Freq) 
GREEN = GPIO.PWM(LED_Green, Freq)
RED.start(0)  
GREEN.start(0)
  
# This function generate the actually color
# You can change the color with the specific color variable.
# After the configuration of the color is finished, you will time.sleep to
# configure how long the specific will be displayed.
 
def LED_color(Red, Green, pause):
    RED.ChangeDutyCycle(Red)
    GREEN.ChangeDutyCycle(Green)
    sleep(pause)
 
    RED.ChangeDutyCycle(0)
    GREEN.ChangeDutyCycle(0)
   
print "LED-Test [press ctrl+c to end the test]"
  
# Main program loop:
# The task of this loop is to create for every single color an own variable.
# By mixing the brightness levels of the colors, you will get a color gradient.
try:
    while True:
        for x in range(0,2):
            for y in range(0,2):
                print (x,y)
                for i in range(0,101):
                    LED_color((x*i),(y*i),.02)
   
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