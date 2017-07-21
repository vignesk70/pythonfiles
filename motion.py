from gpiozero import MotionSensor,LED
from time import sleep

pir = MotionSensor(4,queue_len=5,threshold=0.7)
led = LED(17)
i=0
led.on()
sleep(60)
led.off()

def detected():
	print("Motion detected")
	led.on()
def undetected():
	print("No motion")
	led.off()

while True:
	pir.when_motion = detected()
	pir.when_no_motion = undetected()
	
        
