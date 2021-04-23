import RPi.GPIO as GPIO 
import time 

GPIO.setmode(GPIO.BCM)

def start_up():
    print ("Welcome to Raspberry Pi Network Monitor.")
    accept = input("Would you like to continue? (y/n)").lower().strip()
    if accept == "y":
        RPi.start(GPIO.BCM)
    else:
        print ("See you next time")
        RPi.off(GPIO.BCM)

