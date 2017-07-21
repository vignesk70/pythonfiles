from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.rotation = 180


#camera.start_preview()
sleep(2)
picpath='/home/pi/Desktop/image.jpg'
camera.capture(picpath)
#camera.stop_preview()
camera.close()

