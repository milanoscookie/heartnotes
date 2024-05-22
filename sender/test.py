
import time
import RPi.GPIO as GPIO
from i2s_mono import *
from azure.iot.device import IoTHubDeviceClient, Message
import json

# from https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/
# https://github.com/makerportal/rpi_i2s
# https://makersportal.com/blog/recording-stereo-audio-on-a-raspberry-pi

CONNECTION_STRING = "HostName=milan-iothub.azure-devices.net;DeviceId=sender-heartnotes;SharedAccessKey=/Nxx9g90sMp9ZHQrI4tRu2L9aW43T/oH/PILnQ56FPI="

def send_data_to_azure(data):
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    message = Message(json.dumps(data))
    client.send_message(message)
    print("Message successfully sent")

def test_cb():
    send_data_to_azure("heyhey")

if __name__ == '__main__':
    while True:
        test_cb()
        time.sleep(1000)
