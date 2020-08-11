#!/usr/bin/env python
# -*- coding: utf-8 -*-

import OPi.GPIO as GPIO

import time          # this lets us have a time delay

GPIO.setboard(GPIO.PCPCPLUS)
GPIO.setmode(GPIO.BOARD)

# Declaration and initialisation of the input pins which are connected with the sensor.
PIN_CLK = 13
PIN_DT = 12
BUTTON_PIN = 11
 
GPIO.setup(PIN_CLK, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(PIN_DT, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
 
# Needed variables will be initialised
Counter = 0
Richtung = True
PIN_CLK_LETZTER = 0
PIN_CLK_AKTUELL = 0
delayTime = 0.01
 
# Initial reading of Pin_CLK
PIN_CLK_LETZTER = GPIO.input(PIN_CLK)
 
# This output function will start at signal detection
def outFunction(null):
    global Counter
 
    PIN_CLK_AKTUELL = GPIO.input(PIN_CLK)
 
    if PIN_CLK_AKTUELL != PIN_CLK_LETZTER:
 
        if GPIO.input(PIN_DT) != PIN_CLK_AKTUELL:
            Counter += 1
            Richtung = True
        else:
            Richtung = False
            Counter = Counter - 1
 
        print ("Rotation detected: ")
 
        if Richtung:
            print ("Rotational direction: Clockwise")
        else:
            print ("Rotational direction: Counterclockwise")
 
        print ("Current position: ", Counter)
        print "------------------------------"
 
def CounterReset(null):
    global Counter
 
    print ("Position reset!")
    print ("------------------------------")
    Counter = 0
 
# To include a debounce directly, the output function will be initialised from the GPIO Python Module via callback-option
GPIO.add_event_detect(PIN_CLK, GPIO.BOTH, callback=outFunction, bouncetime=50)
GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=CounterReset, bouncetime=50)
 
 
print ("Sensor-Test [press ctrl-c to end]")
 
# Main program loop
try:
        while True:
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