
import class_for_audio
#from convert_to_rgb import *

song1 = class_for_audio.SongToRgb("song1.mp3")
song1.convert_to_numerical()
wv = song1.get_array_splitwaves(15)

for i in range(len(wv)):
    print(str(wv[i]))


