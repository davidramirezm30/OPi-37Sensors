import OPi.GPIO as GPIO
import glob
import time
from time import sleep

GPIO.setboard(GPIO.PCPCPLUS)    # Orange Pi PC board
GPIO.setmode(GPIO.BOARD)
 
# here you can modify the break between the measurements
sleeptime = 1
 
# the one-wire input pin will be declared and the integrated pullup-resistor will be enabled
GPIO_PIN = 3
GPIO.setup(GPIO_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
 
# After the enabling of the pullup-resistor you have to wait till the communication with the DS18B20 sensor has started
print ('wait for initialisation...')
 
base_dir = '/sys/bus/w1/devices/'
while True:
    try:
        device_folder = glob.glob(base_dir + '28*')[0]
        break
    except IndexError:
        sleep(0.5)
        continue
device_file = device_folder + '/w1_slave'
 
 
# The function to read currently measurement at the sensor will be defined.
def TemperaturMessung():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
# To initialise, the sensor will be read "blind"
TemperaturMessung()
 
# Analysis of temperature: At the Raspberry Pi
# noticed one-wire slaves at the directory /sys/bus/w1/devices/
# will be assigned to a own subfolder.
# In this folder is the file in which the data from the one-wire bus will be saved.<br /># In this function, the data will be analyzed, the temperature read and returned to the main program.<br />
def TemperaturAuswertung():
    lines = TemperaturMessung()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = TemperaturMessung()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c
 
# main program loop
# The measured temperature will be displayed via console, between the measurements is a break.
# The break time can be configured by the variable "sleeptime"
try:
    while True:
        print ('---------------------------------------')
        print ("Temperature:", TemperaturAuswertung(), "C")
        time.sleep(sleeptime)
# Scavenging work after the end of the program
except KeyboardInterrupt:  
    # here you put any code you want to run before the program   
    # exits when you press CTRL+C  
    print ("An error or exception occurred!")
  
except:  
    # this catches ALL other exceptions including errors.  
    # You won't get any error messages for debugging  
    # so only use it once your code is working  
    print ("Other error or exception occurred!" ) 
  
finally:  
    GPIO.cleanup() # this ensures a clean exit 
    if humid is not None and temper is not None:

        # The result will be shown at the console
        print("temperature = {0:0.1f}C  | rel. humidity = {1:0.1f}%".format(temper, humid))
     
    # Because of the linux OS, the Raspberry Pi has problems with realtime measurements.
    # It is possible that, because of timing problems, the communication fails.
    # In that case, an error message will be displayed - the result should be shown at the next try.
    else:
        print('Error while reading - please wait for the next try!')
    print("-----------------------------------------------------------------")
    print("")
    time.sleep(sleeptime)
         
