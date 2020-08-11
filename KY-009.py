#!/usr/bin/env python
# -*- coding: utf-8 -*-

import OPi.GPIO as GPIO

import random
from time import sleep          # this lets us have a time delay

GPIO.setboard(GPIO.PCPCPLUS)
GPIO.setmode(GPIO.BOARD)

# The output pins will be declared, which are connected with the LEDs. 
LED_Red = 31
LED_Green = 33
LED_Blue = 35
 
# Set pins to output mode
GPIO.setup(LED_Red, GPIO.OUT) 
GPIO.setup(LED_Green, GPIO.OUT)
GPIO.setup(LED_Blue, GPIO.OUT)
   
Freq = 100 #Hz
# The different colors will be initialized.
RED = GPIO.PWM(LED_Red, Freq) 
GREEN = GPIO.PWM(LED_Green, Freq)
BLUE = GPIO.PWM(LED_Blue, Freq)
RED.start(0)  
GREEN.start(0)
BLUE.start(0)
# This function generate the actually color<br /># You can change the color with the specific color variable.<br /># After the configuration of the color is finished, you will use time.sleep to<br /># configure how long the specific color will be displayed.  
  
def LED_color(Red, Green, Blue, pause):
    RED.ChangeDutyCycle(Red)
    GREEN.ChangeDutyCycle(Green)
    BLUE.ChangeDutyCycle(Blue)
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
                for z in range(0,2):
                    print (x,y,z)
                    for i in range(0,101):
                        LED_color((x*i),(y*i),(z*i),.02)
   
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