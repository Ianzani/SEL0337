from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation=180

camera.start_preview()
input()
camera.stop_preview()