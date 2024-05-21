
import time
import RPi.GPIO as GPIO
from i2s_mono import *

# from https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/
# https://github.com/makerportal/rpi_i2s
# https://makersportal.com/blog/recording-stereo-audio-on-a-raspberry-pi

RES_TOUCH_GPIO = 17

def record_audio_cb():
    audio_rec()

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RES_TOUCH_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(RES_TOUCH_GPIO, GPIO.RISING, callback=record_audio_cb, bouncetime=50)

    while True:
        GPIO.input(1)
