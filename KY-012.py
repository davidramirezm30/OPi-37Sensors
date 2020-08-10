#Needed modules will be imported and configured.
import orangepi.pc
from OPi import GPIO

from time import sleep          # this lets us have a time delay

GPIO.setmode(orangepi.pc.BOARD)
 
# Output pin declaration for the Buzzer.
Buzzer_PIN = 7
GPIO.setup(Buzzer_PIN, GPIO.OUT, initial= GPIO.LOW)
    
print ("Buzzer-test [press ctrl+c to end the test]")
   
# Main program loop
try:
        while True:
            print("Buzzer will be on for 4 seconds")
            GPIO.output(Buzzer_PIN,GPIO.HIGH) #Buzzer will be switched on
            sleep(4) #Waitmode for 4 seconds
            print("Buzzer will be off for 4 seconds") 
            GPIO.output(Buzzer_PIN,GPIO.LOW) #Buzzer will be switched off 
            sleep(2) #Waitmode for another 2 seconds in which the buzzer will be off
         
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