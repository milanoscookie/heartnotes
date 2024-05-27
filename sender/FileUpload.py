import os
from azure.iot.device import IoTHubDeviceClient
from azure.core.exceptions import AzureError
from azure.storage.blob import BlobClient

CONNECTION_STRING = "HostName=milan-iothub.azure-devices.net;DeviceId=sender-heartnotes;SharedAccessKey=/Nxx9g90sMp9ZHQrI4tRu2L9aW43T/oH/PILnQ56FPI="
PATH_TO_FILE = r"audio_out.wav"

def store_blob(blob_info, file_name):
    try:
        sas_url = "https://{}/{}/{}{}".format(
            blob_info["hostName"],
            blob_info["containerName"],
            blob_info["blobName"],
            blob_info["sasToken"]
        )

        print("\nUploading file: {} to Azure Storage as blob: {} in container {}\n".format(file_name, blob_info["blobName"], blob_info["containerName"]))

        # Upload the specified file
        with BlobClient.from_blob_url(sas_url) as blob_client:
            with open(file_name, "rb") as f:
                result = blob_client.upload_blob(f, overwrite=True)
                return (True, result)

    except FileNotFoundError as ex:
        # catch file not found and add an HTTP status code to return in notification to IoT Hub
        ex.status_code = 404
        return (False, ex)

    except AzureError as ex:
        # catch Azure errors that might result from the upload operation
        return (False, ex)

    
def run_sample(device_client, path_to_file):
    # Connect the client
    device_client.connect()

    # Get the storage info for the blob
    blob_name = os.path.basename(path_to_file)

    storage_info = device_client.get_storage_info_for_blob(blob_name)

    # Upload to blob
    success, result = store_blob(storage_info, path_to_file)

    if success == True:
        print("Upload succeeded. Result is: \n") 
        print(result)
        print()

        device_client.notify_blob_upload_status(
            storage_info["correlationId"], True, 200, "OK: {}".format(path_to_file)
        )

    else :
        # If the upload was not successful, the result is the exception object
        print("Upload failed. Exception is: \n") 
        print(result)
        print()

        device_client.notify_blob_upload_status(
            storage_info["correlationId"], False, result.status_code, str(result)
        )

def send_file_to_azure(con_str, file_path):
    device_client = IoTHubDeviceClient.create_from_connection_string(con_str)

    try:
        print ("IoT Hub file upload sample, press Ctrl-C to exit")
        run_sample(device_client, file_path)
    except KeyboardInterrupt:
        print ("IoTHubDeviceClient sample stopped")
    finally:
        # Graceful exit
        device_client.shutdown()

