
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
from azure.iot.device import IoTHubDeviceClient
from azure.core.exceptions import AzureError
from azure.storage.blob import BlobClient

# from https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/
# https://github.com/makerportal/rpi_i2s
# https://makersportal.com/blog/recording-stereo-audio-on-a-raspberry-pi

CONNECTION_STRING = "HostName=milan-iothub.azure-devices.net;DeviceId=sender-heartnotes;SharedAccessKey=/Nxx9g90sMp9ZHQrI4tRu2L9aW43T/oH/PILnQ56FPI="
PATH_TO_FILE = r"/home/milan/ce495/heartnotes/sender/heyey.txt"

async def main():

    # Create instance of the device client using the connection string
    device_client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

    await upload(device_client)
    # # Connect the device client.
    # await device_client.connect()

    # # Send a single message
    # print("Sending message...")
    # await device_client.send_message("0.5")
    # print("Message successfully sent!")

    # Finally, shut down the client
    # await device_client.shutdown()

async def store_blob(blob_info, file_name):
    try:
        sas_url = "https://{}/{}/{}{}".format(
            blob_info["hostName"],
            blob_info["containerName"],
            blob_info["blobName"],
            blob_info["sasToken"]
        )

        # Upload the specified file
        with await BlobClient.from_blob_url(sas_url) as blob_client:
            with await open(file_name, "rb") as f:
                await blob_client.upload_blob(f, overwrite=True)
    except:
        print("u suck, ur code doesnt work")


async def upload():

    device_client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

    # Connect the client
    await device_client.connect()

    # Get the storage info for the blob
    blob_name = os.path.basename(PATH_TO_FILE)
    storage_info = device_client.get_storage_info_for_blob(blob_name)

    # Upload to blob
    await store_blob(storage_info, PATH_TO_FILE)

    await device_client.shutdown()

if __name__ == "__main__":
    asyncio.run(upload())
