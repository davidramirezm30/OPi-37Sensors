#!/usr/bin/env python
# -*- coding: utf-8 -*-

import OPi.GPIO as GPIO
from time import sleep          # this lets us have a time delay

GPIO.setboard(GPIO.PCPCPLUS)    # Orange Pi PC board
GPIO.setmode(GPIO.BOARD)
  
# Declaration of the break between the changes of the relay status (in seconds)
delayTime = 1
 
# Declaration of the input pin which is connected with the sensor. Additional to that, the pullup resistor will be activated.
RELAIS_PIN = 22
GPIO.setup(RELAIS_PIN, GPIO.OUT)
GPIO.output(RELAIS_PIN, False)
 
print "Sensor-test [press ctrl+c to end]"
 
 
# Main program loop
try:
        while True:
            GPIO.output(RELAIS_PIN, True) # NO is now connected through
            time.sleep(delayTime)
            GPIO.output(RELAIS_PIN, False) # NC is now connected through
            time.sleep(delayTime)
 

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
