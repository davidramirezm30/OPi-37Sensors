# Needed modules will be imported and configured.
import OPi.GPIO as GPIO

import time
   
GPIO.setboard(GPIO.PCPCPLUS)
GPIO.setmode(GPIO.BOARD)
   
# Declaration of the LED and sensor pins
#LED_PIN = 15
Sensor_PIN = 22
GPIO.setup(Sensor_PIN, GPIO.IN)
#GPIO.setup(LED_PIN, GPIO.OUT)
   
print ("Sensor-test [press ctrl+c to end the test]")
   
# This output function will be started at signal detection
def outFunction(null):
        GPIO.output(LED_PIN, True)
   
# This output function will be started at signal detection 
GPIO.add_event_detect(Sensor_PIN, GPIO.FALLING, callback=outFunction, bouncetime=10) 
   
# main program loop 
try:
        while True:
            time.sleep(1)
        # output will be reseted if the switch turn back to the default position.
        if GPIO.input(Sensor_PIN):
            GPIO.output(LED_PIN,False)
   
# Scavenging work after the program has ended
except KeyboardInterrupt:
        GPIO.cleanup()