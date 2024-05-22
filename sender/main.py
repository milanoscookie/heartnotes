
import time
import os
import RPi.GPIO as GPIO
from gpiozero import Button
from recording_test import *

# from azure.iot.device import IoTHubDeviceClient, Message
#from azure.iot.device import IoTHubDeviceClient, Message
import json

# from https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/
# https://github.com/makerportal/rpi_i2s
# https://makersportal.com/blog/recording-stereo-audio-on-a-raspberry-pi

RES_TOUCH_GPIO = 17
CONNECTION_STRING = "HostName=milan-iothub.azure-devices.net;DeviceId=sender-heartnotes;SharedAccessKey=/Nxx9g90sMp9ZHQrI4tRu2L9aW43T/oH/PILnQ56FPI="

def send_data_to_azure(data):
    #client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    #message = Message(json.dumps(data))
    #client.send_message(message)
    print("Message successfully sent")

def record_audio():
    record_stream()
    #send_data_to_azure("heyhey")

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RES_TOUCH_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)


    while True:
        if (GPIO.input(RES_TOUCH_GPIO)):
            record_audio()
            time.sleep(2)