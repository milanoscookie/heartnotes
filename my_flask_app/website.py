from flask import Flask, render_template
from azure.storage.blob import BlobServiceClient
import os
import datetime

app = Flask(__name__)
# app= Flask(__name__, template_folder='heartnotes')    
# CORS(app)

# Azure Blob Storage credentials
AZURE_STORAGE_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=storagemsgmsg;AccountKey=zxsrftvcmdyVWSuhP//jx7WhBBNf8McbJEo5B4xjupWhWzu+0MvhdIlTVtL9rhyw8dNW1vRm3roV+AStazZXVw==;EndpointSuffix=core.windows.net"
CONTAINER_NAME = "containermsgmsg"
STORAGE_ACCOUNT_NAME = "storagemsgmsg"
SAS_TOKEN = "sp=racwdli&st=2024-05-23T01:35:31Z&se=2026-05-23T09:35:31Z&sv=2022-11-02&sr=c&sig=A0b718VBGZy%2F2Lm9S0JMYkowG6WZtNz7r%2Bg2ERi3UR0%3D"

blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)
container_client = blob_service_client.get_container_client(CONTAINER_NAME)

@app.route('/')
def home():
    # List blobs in the container
    blob_list = container_client.list_blobs()
    audio_files = []
    times = []
    for blob in blob_list:
        # Construct the URL for each audio file
        print(blob.name[len(blob.name) - 3:])
        if (blob.name[len(blob.name) - 3:] == "wav"):
            audio_url = f"https://{STORAGE_ACCOUNT_NAME}.blob.core.windows.net/{CONTAINER_NAME}/{blob.name}?{SAS_TOKEN}"
            print("blob:" + str(blob))
            print("blob.name: ")
            print(blob.name)
            audio_files.append(audio_url)
            creation_time = blob['creation_time'].strftime("%Y-%m-%d %H:%M:%S")
            times.append(creation_time)
            print(blob['creation_time'])
            print(creation_time)
            print(audio_files)
    return render_template('audio.html', audio_files=audio_files, times = times)

if __name__ == '__main__':
    app.run(debug=True)