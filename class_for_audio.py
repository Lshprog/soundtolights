import librosa
import numpy
from pydub import AudioSegment
import numpy as np
from convert_to_rgb import *

class SongToRgb:
    def __init__(self,path):
        self.audio = audio = AudioSegment.from_file(path, format="mp3")

    # convert to numerical data
    def convert_to_numerical(self) -> np.ndarray:
        data = np.array(self.audio.get_array_of_samples(), dtype=np.float32) / 2 ** 15
        return data

    # calculate sample rate
    def get_sample_rate(self):
        return self.audio.frame_rate

    # splitting an array into pieces of length = times
    def get_array_splitwaves(self,times) -> np.ndarray:
        sample_rate = self.get_sample_rate()
        data = self.convert_to_numerical()

        # create an array of wavelengths of samples
        wavelengths = abs(1 / (sample_rate * data)) * 10 ** 6

        lengthofwv = int(len(wavelengths)/times)
        newarr = np.array_split(wavelengths, lengthofwv)
        wv = np.empty(lengthofwv)

        for i in range(lengthofwv):
            wv[i] = newarr[i].sum() / len(newarr[i])

        return wv

