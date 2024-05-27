import sounddevice as sd
import numpy as np
import wave
import time
import soundfile as sf

# Set the duration of the recording in seconds
DURATION = 6

# Define the sample rate and other audio parameters
sample_rate = 44100
channels = 1  # Mono recording

# Define a callback function for recording audio
def callback(indata, frames, time, status):
    if status:
        print('Error:', status)
    # Save the recorded audio data to a numpy array
    recorded_data.append(indata.copy())

# Initialize an empty list to store recorded audio data

def record_stream():
    recorded_data = []

    print('Recording started...')
    audio_data = sd.rec(int(DURATION * sample_rate), samplerate=sample_rate, channels=channels, device='hw:3,0')
    sd.wait()  # Wait until recording is finished
    print('Recording stopped')

    # Save the recorded audio to a WAV file
    output_file = 'audio_out.wav'
    sf.write(output_file, audio_data, sample_rate)

    print(f'Recording saved as {output_file}')

    return output_file
