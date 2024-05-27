
import time
import os
import RPi.GPIO as GPIO
from gpiozero import Button
from recording_test import *
from azure.core.exceptions import AzureError
from azure.storage.blob import BlobClient
from FileUpload import *
import paho.mqtt.client as mqtt

from azure.iot.device import IoTHubDeviceClient, Message
import json
import requests

import socket

HOST = '10.106.14.75'  # IP address of the ESP32
PORT = 8888  # Choose a free port number

# ESP32 IP address and endpoint
esp32_ip = "http://10.106.14.75/data"

# Data to send
data = "Hello, ESP32!"

# from https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/
# https://github.com/makerportal/rpi_i2s
# https://makersportal.com/blog/recording-stereo-audio-on-a-raspberry-pi

RES_TOUCH_GPIO = 17
CONNECTION_STRING = "HostName=milan-iothub.azure-devices.net;DeviceId=sender-heartnotes;SharedAccessKey=/Nxx9g90sMp9ZHQrI4tRu2L9aW43T/oH/PILnQ56FPI="

def send_data_to_azure(file_name):
    send_file_to_azure(CONNECTION_STRING, file_name)
    print("Message successfully sent")

def record_audio():
    output_file = record_stream()
    return output_file

def send_message_to_iot_hub(message):
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    client.connect()
    msg = Message(message)
    client.send_message(msg)
    print(f"Message sent: {message}")
    client.shutdown()

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # client.subscribe("topic", qos=0)  # Subscribe to the topic with QoS 0

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RES_TOUCH_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
    while True:
        if (GPIO.input(RES_TOUCH_GPIO)):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                byte_to_send = b'\x08'  # Example byte to send (ASCII 'A')
                s.sendall(byte_to_send)     
            
            send_message_to_iot_hub("Touch sensor pressed!")
            file_out = record_audio()
            send_data_to_azure(file_out)

            time.sleep(2)

        #print(GPIO.input(RES_TOUCH_GPIO))



        

