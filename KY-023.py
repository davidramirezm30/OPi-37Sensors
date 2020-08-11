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
delayTime = 0.05 # in seconds

ser = Serial('/dev/ttyS3', 9600)

ser.flushInput()
ser.flushOutput()
    
# Input pin for the digital signal will be picked here
Button_PIN = 40 #SW
GPIO.setup(Button_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
  
#############################################################################################################
  
# ########
# main program loop
# ########
# The program reads the current value of the input pin
# and shows it at the terminal
  
try:
    while True:
        x = ser.readline().split('J1 VRx ', 2)
        #print x, "XXXXXXXXXX"
        y = ser.readline().split('J1 VRy ', 2)
        #print y, "YYYYYYYYYY"
        if GPIO.input(Button_PIN) == True:
            if '' in x:
                print ''
            if '' in y:
                # Output at the terminal
                print ("X-axis (mV):", VRx,"Y-axis (mV):", VRy,"Button: not pushed")
        else:
            if '' in x:
                VRx = x[1]
            if '' in y:
                VRy = y[1]
                print ("X-axis (mV):", VRx,"Y-axis (mV):", VRy,"Button: pushed")
            
        print ("---------------------------------------")

        # Reset + Delay
        button_pressed = False
        sleep(delayTime)

  
except KeyboardInterrupt:
        GPIO.cleanup()