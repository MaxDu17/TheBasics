import librosa
import soundfile as sf

#librosa has problems with mp3 files
file, sr = librosa.load("samples/sample.ogg")
print("done loading librosa")
sf.write("samples/sample_written.wav", data = file, samplerate = sr)
print("done saving librosa")


#how about wave files? We can use librosa, or we can use the "wave" library
import wave
wf = wave.open("samples/sample.wav", "rb")

wf_write = wave.open("samples/sample_written_wave.wav", "wb")
wf_write.setnchannels(1)
wf_write.setsampwidth(2) #byte width
wf_write.setframerate(sr)

#WARNING: this does NOT copy the audio correctly. Librosa is your safer bet
data = wf.readframes(1024)
while len(data) > 0:
    data = wf.readframes(1024) #raw bytes buffer
    wf_write.writeframes(data)

print("done reading and writing through wave")
