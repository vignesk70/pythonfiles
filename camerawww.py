from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.rotation = 180


#camera.start_preview()
sleep(2)
picpath='/var/www/media/image.jpg'
camera.capture(picpath)
#camera.stop_preview()
camera.close()

