import numpy as np

import class_for_audio
from matplotlib import pyplot as plt
import numpy

import convert_to_rgb


song1 = class_for_audio.SongToRgb("song1.mp3")
song1.convert_to_numerical()
wv = song1.get_array_splitwaves(15)

y = numpy.arange(0,len(wv))
plt.plot(y,wv)
plt.show()



for i in range(len(wv)):
    print(str(convert_to_rgb.wave2rgb(wv[i])))




