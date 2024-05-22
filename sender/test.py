
import time
from azure.iot.device import IoTHubDeviceClient, Message
import json
import asyncio
import uuid
from azure.iot.device.aio import IoTHubModuleClient
from azure.iot.device import Message
import os
import asyncio
from azure.iot.device.aio import IoTHubDeviceClient

# from https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/
# https://github.com/makerportal/rpi_i2s
# https://makersportal.com/blog/recording-stereo-audio-on-a-raspberry-pi

CONNECTION_STRING = "HostName=milan-iothub.azure-devices.net;DeviceId=sender-heartnotes;SharedAccessKey=/Nxx9g90sMp9ZHQrI4tRu2L9aW43T/oH/PILnQ56FPI="

async def main():
    # Fetch the connection string from an environment variable
    conn_str = os.getenv(CONNECTION_STRING)

    # Create instance of the device client using the connection string
    device_client = IoTHubDeviceClient.create_from_connection_string(conn_str)

    # Connect the device client.
    await device_client.connect()

    # Send a single message
    print("Sending message...")
    await device_client.send_message("0.5")
    print("Message successfully sent!")

    # Finally, shut down the client
    await device_client.shutdown()


if __name__ == "__main__":
    asyncio.run(main())
    asyncio.run(main())
    asyncio.run(main())