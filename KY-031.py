# Needed modules will be imported and configured
import OPi.GPIO as GPIO
import time

GPIO.setboard(GPIO.PCPCPLUS)    # Orange Pi PC board
GPIO.setmode(GPIO.BOARD)
    
# Declaration of the input pin which is connected with the sensor. Additional to that, a pullup resistor will be activated.
GPIO_PIN = 29
GPIO.setup(GPIO_PIN, GPIO.IN)
    
print "Sensor-test [press ctrl+c to end]"
    
# This outFunction will be started after a signal was detected.
def outFunction(null):
        print("Signal detected")
    
# The outFunction will be started after a signal (falling signal edge) was detected.
GPIO.add_event_detect(GPIO_PIN, GPIO.FALLING, callback=outFunction, bouncetime=100) 
    
# main program loop
try:
        while True:
                time.sleep(1)
    
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
