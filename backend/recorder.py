import sounddevice as sd
import numpy as np
import soundfile as sf

SAMPLERATE = 16000
CHANNELS = 1
DURATION = 60  # in seconds

def record_audio(filename="audio/output.wav"):
    print("Listening for up to 60s or silence...")
    recording = sd.rec(int(DURATION * SAMPLERATE), samplerate=SAMPLERATE, channels=CHANNELS)
    sd.wait()
    volume = np.linalg.norm(recording) * 10
    if volume < 0.1:
        print("Silence detected. Stopping early.")
    sf.write(filename, recording, SAMPLERATE)