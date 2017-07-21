from gpiozero import MotionSensor
from picamera import PiCamera
from datetime import datetime

url = 'http://192.168.21.176:5000/'
camera = PiCamera()
pir = MotionSensor(4)
while True:
    pir.wait_for_motion()
    filename = datetime.now().strftime("%Y-%m-%d_%H.%M.%S.h264")
    camera.start_recording(filename)
    print("Start record ",filename)
    
    pir.wait_for_no_motion()
    camera.stop_recording()
    print("Stop record")
