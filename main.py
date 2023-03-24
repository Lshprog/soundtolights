import librosa
import numpy
from pydub import AudioSegment
import pydub
import numpy as np
from convert_to_rgb import *

# load audio file
audio = AudioSegment.from_file("song1.mp3", format="mp3")

# convert to numerical data
data = np.array(audio.get_array_of_samples(), dtype=np.float32) / 2 ** 15
#data = librosa.resample(data, audio.frame_rate, 44100)
sample_rate = audio.frame_rate
#print(sample_rate)
wavelengths = abs(1 / (sample_rate * data)) * 10 ** 6
#data = data.reshape((-1,audio.channels))

#data = data.astype(np.float32) / 2 ** 15

# convert from stereo to mono
#if audio.channels == 2:
#    data = np.mean(data.reshape(-1, 2), axis=1)

#normalize data to [-1, 1]
#if np.max(data) > 1.0 or np.min(data) < -1.0:
#    data /= np.max(np.abs(data))

# resample to 44.1kHz if necessary
#if audio.frame_rate != 44100:
#    data = librosa.resample(data, audio.frame_rate, 44100)

# convert to NumPy array
#samples = np.array(data, dtype=np.float32)
#samples = np.array(data, dtype=np.int16)

newarr = np.array_split(wavelengths, 1149703)
wv = np.empty(1149703)
for i in range(1149703):
    wv[i] = newarr[i].sum()/len(newarr[i])

#print(len(wavelengths))
for i in range(len(wv)):
    print(str(wv[i])+" ")
#for i in range(len(wv)):
#    print(str(wave2rgb(wv[i])))
#print(min(wavelengths))
#print(max(wavelengths))
