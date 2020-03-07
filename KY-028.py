import time
from time import sleep

import serial
from serial import Serial

import math, signal, sys, os
import OPi.GPIO as GPIO
GPIO.setboard(GPIO.PCPCPLUS)
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
 
# initialise variables
delayTime = 0.5 # in seconds

ser = Serial('/dev/ttyS3', 9600)

ser.flushInput()
ser.flushOutput()
    
# Input pin for the digital signal will be picked here
Digital_PIN = 22
GPIO.setup(Digital_PIN, GPIO.IN, pull_up_down = GPIO.PUD_OFF)
  
#############################################################################################################
  
# ########
# main program loop
# ########
# The program reads the current value of the input pin
# and shows it at the terminal
  
try:
    while True:
        val = ser.readline()
        if 'J7' in val:
            # Output at the terminal
            if GPIO.input(Digital_PIN) == False:
                    print "Analog voltage value:", val,"mV, ","extreme value: not reached"
            else:
                    print "Analog voltage value:", val, "mV, ", "extreme value: reached"
            print "---------------------------------------"

            sleep(delayTime)
  
  
  
except KeyboardInterrupt:
        GPIO.cleanup()