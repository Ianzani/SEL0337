#Nomes: Gabriel Domingues       NUSP:11800903
#       Ian Zaniolo Sirbone     NUSP:04735640
#Código Camera

from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation=180
camera.resolution=(1024, 768)

#====================Código captura de imagem============================

#camera.start_preview()
#camera.annotate_text="Gabriel Montgani NUSP:11800903\n Ian Zaniolo NUSP:4735640"
#sleep(2)
#camera.capture('/home/sel/SEL0337_Gabriel_Ian/SEL0337/image.jpg')
#camera.stop_preview()


#====================Código captura de video=============================

camera.start_preview()
camera.annotate_text="Gabriel Montgani NUSP:11800903\n Ian Zaniolo NUSP:4735640"
camera.start_recording('/home/sel/SEL0337_Gabriel_Ian/SEL0337/video.h264')
sleep(5)
camera.stop_recording()
camera.stop_preview()