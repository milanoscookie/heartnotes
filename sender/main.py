
import time
import RPi.GPIO as GPIO
from i2s_mono import *
# from azure.iot.device import IoTHubDeviceClient, Message

# from https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/
# https://github.com/makerportal/rpi_i2s
# https://makersportal.com/blog/recording-stereo-audio-on-a-raspberry-pi

RES_TOUCH_GPIO = 17
CONNECTION_STRING = "YourIoTHubDeviceConnectionString"

# def send_data_to_azure(data):
#     client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
#     message = Message(json.dumps(data))
#     client.send_message(message)
#     print("Message successfully sent")

def record_audio_cb():
    file_name = audio_rec()
    # send_data_to_azure(file_name)

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RES_TOUCH_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(RES_TOUCH_GPIO, GPIO.RISING, callback=record_audio_cb, bouncetime=50)
