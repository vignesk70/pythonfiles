import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO_OUT=25

print("Temp measure in progress")
GPIO.setup(GPIO_OUT,GPIO.IN)

