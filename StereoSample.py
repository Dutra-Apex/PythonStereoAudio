import math
import wave
import struct

freq = 220.0
freq2 = 440.0

data_size = 10000
fname = "TestSample.wav"

#framerate of the sound
frate = 21025.0  

amp = 44000.0   

#Creates a
sine_list_x = []
for x in range(data_size):
    sine_list_x.append(math.sin(2*math.pi*freq*(x/frate)))
for x in range(data_size):
    sine_list_x.append(math.sin(2*math.pi*freq2*(x/frate)))


sine_list_y = []
for x in range(data_size):
    sine_list_y.append(math.sin(2*math.pi*freq2*(x/frate)))
for x in range(data_size):
    sine_list_y.append(math.sin(2*math.pi*freq*(x/frate)))


wav_file = wave.open(fname, "w")

nchannels = 2
sampwidth = 2
framerate = int(frate)
nframes = data_size
comptype = "NONE"
compname = "not compressed"

wav_file.setparams((nchannels, sampwidth, framerate, nframes,
    comptype, compname))

for s, t in zip(sine_list_x, sine_list_y):
    # write the audio frames to file
    wav_file.writeframes(struct.pack('h', int(s*amp/2)))
    wav_file.writeframes(struct.pack('h', int(t * amp / 2)))

wav_file.close()
