import sounddevice
from scipy.io.wavfile import write

print("Recording Started…")
recording = sounddevice.rec((10 * 44100), samplerate= 44100, channels=2)
sounddevice.wait()
write("record.wav", 44100, recording)
print("Recording Finished")