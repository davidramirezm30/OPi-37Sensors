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

#############################################################################################################
  
# ########
# main program loop
# ########
# The program reads the current value of the input pin
# and shows it at the terminal
  
try:
    while True:
        val = ser.readline()
        if 'J5' in val:
            print ("Analog voltage value:", val, "mV")
            print ("---------------------------------------")

            sleep(delayTime)
  
  
  
except KeyboardInterrupt:
        GPIO.cleanup()