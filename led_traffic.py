from gpiozero import LED
from time import sleep
from signal import pause

redled = LED(23)
yellowled=LED(24) 
greenled=LED(25)

redled.off()
yellowled.off()
greenled.off,

while True:
	redled.on()
	sleep(1)
	redled.off()

	yellowled.on()
	sleep(1)
	yellowled.off()
	greenled.on()
	sleep(1)
	greenled.off()

