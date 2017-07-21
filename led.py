from gpiozero import LED
from time import sleep
from signal import pause

led = LED(17)

led.off()

while True:
	led.on()
	sleep(1)
	led.off()
	sleep(1)

