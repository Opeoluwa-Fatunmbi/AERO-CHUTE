'''
It is a natural instinct to scream and panick when there is a sudden emergency on a plane
This feature is to monitor the scream level of the passengers on board
'''

import sounddevice as sd
import numpy as np

def loud_noise_detector(threshold=5000, duration=0.5):
    # Set the recording parameters
    sr = 44100  # Sample rate
    chunk = int(sr * duration)  # Number of samples per chunk
    
    while True:
        # Record audio
        data = sd.rec(chunk, sr)
        sd.wait()  # Wait for recording to finish
        
        # Calculate the RMS (root mean square) of the audio data
        rms = np.sqrt(np.mean(data**2))
        
        # Compare the RMS value to the threshold
        if rms > threshold:
            print("Loud noise detected!")

# Call the function
loud_noise_detector()

