import time
from time import sleep

import serial
from serial import Serial

import math, signal, sys, os
import orangepi.pc
from OPi import GPIO

GPIO.setboard(GPIO.PCPCPLUS)
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
 
# initialise variables
delayTime = 0.5 # in seconds

ser = Serial('/dev/ttyS3', 9600)

ser.flushInput()
ser.flushOutput()

port = 'J4'
  
#############################################################################################################

def calcTemp(voltage):
    temperature = math.log((10000/voltage)*(3300-voltage))
    temperature = 1 / (0.001129148 + (0.000234125 + (0.0000000876741 * temperature * temperature)) * temperature);
    #temperature = temperature - 273.15;
    return temperature

# ########
# main program loop
# ########
# The program reads the current value of the input pin
# and shows it at the terminal
  
try:
    while True:
        #val = ser.readline()
        val = ser.readline().split(port, 2)
        
        if '' in val:
            #read voltage-value and calculate temperature
            temp = round(calcTemp(float(val[1])), 2)
            # print to console
            print ("Temperatura:", temp, "C")
            print ("---------------------------------------")

            sleep(delayTime)
             
  
except KeyboardInterrupt:
        GPIO.cleanup()