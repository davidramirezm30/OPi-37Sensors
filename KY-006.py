#Needed modules will be imported and configured.
import OPi.GPIO as GPIO

GPIO.setboard(GPIO.PCPCPLUS)
GPIO.setmode(GPIO.BOARD)
 
#The output pin, which is connected with the buzzer, will be declared here.
GPIO_PIN = 7
GPIO.setup(GPIO_PIN, GPIO.OUT)
#The software-PWM module will be initialized - a frequency of 500Hz will be taken as default.
Frequenz = 500 #In Hertz
pwm = GPIO.PWM(GPIO_PIN, Frequenz)
pwm.start(50)
# The program will wait for the input of a new PWM-frequency from the user.
# Until then, the buzzer will be used with the before inputted frequency (default 500Hz).
try:
    while(True):
        print ("----------------------------------------")
        print ("Current frequency: %d" % Frequenz)
        Frequenz = input("Please input a new frequency (50-5000):")
        pwm.ChangeFrequency(Frequenz)
         
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
