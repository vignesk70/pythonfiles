from gpiozero import MotionSensor
from signal import pause

pir = MotionSensor(4)
pir.wait_for_motion()
print("Motion detected!")
pause()
