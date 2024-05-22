import time
import RPi.GPIO as GPIO
import haptic
from azure.iot.device import IoTHubDeviceClient, Message

# from https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/
# https://github.com/makerportal/rpi_i2s
# https://makersportal.com/blog/recording-stereo-audio-on-a-raspberry-pi

MOTOR_GPIO = 99 # TODO CHANGE
CONNECTION_STRING = "TODO :("

def message_handler(message):
    # print data from both system and application (custom) properties
    for property in vars(message).items():
        print ("    {}".format(property))

    p = float(message['amnt'])
    if(p != 0): haptic.run(p)

def main():
    haptic.setup()
    print("Starting the Python IoT Hub C2D Messaging device sample...")

    # Instantiate the client
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

    print("Waiting for C2D messages, press Ctrl-C to exit")
    while(1):
        try:
            # Attach the handler to the client
            client.on_message_received = message_handler

            while True:
                time.sleep(100)

        except KeyboardInterrupt:
            print("IoT Hub C2D Messaging device sample stopped")

    client.shutdown()