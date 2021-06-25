import math
import wave
import struct

#Increments the frequency of the sound every milisecond
inc = .00002

def sound_wave(freq, frate, size):

    wave = []
    for x in range(size):
        wave.append(math.sin(2*math.pi*freq*(x/frate)))
        #freq = freq + inc
    '''
    for x in range(size//2):
        wave.append(math.sin(2*math.pi*freq*(x/frate)))
        freq = freq - inc
'''
    return wave

#Frequency of the channels
freq = 320.0
freq2 = 440.0

#Number of values in each channel
data_size = 200000

#Framerate (how fast it goes through data_size)
frate = 31025.0 

#Amplitude (volume)
ampr = 5000.0     
ampl = 30000.0

fname = "WaveTest.wav"

nchannels = 2
sampwidth = 2
framerate = int(frate)
nframes = data_size
comptype = "NONE"
compname = "not compressed"

wav_file = wave.open(fname, "w")

wav_file.setparams((nchannels, sampwidth, framerate, nframes,
    comptype, compname))

# Creates the soundwave for both left and right channels
rsound = sound_wave(freq, frate, data_size)
lsound = sound_wave(freq2, frate, data_size)

print(len(rsound))

incr = 0.1
incl = 0.52

'''
for s, t in zip(rsound, lsound):
    # write the audio frames to file
    wav_file.writeframes(struct.pack('h', int(s * ampl / 2)))
    wav_file.writeframes(struct.pack('h', int(t * ampl / 2)))
    #ampl += incr
'''

#Increments the left side amplitude for the first third of the sound
for s, t in zip(rsound[:(len(rsound)//3)], lsound[:(len(lsound)//3)]):
    # write the audio frames to file
    wav_file.writeframes(struct.pack('h', int(s * ampr / 2)))
    wav_file.writeframes(struct.pack('h', int(t * ampl / 2)))
    ampl += incr

for s, t in zip(rsound[(len(rsound)//3):((len(rsound)//3)*2)], lsound[(len(lsound)//3):((len(lsound)//3)*2)]):
    # write the audio frames to file
    wav_file.writeframes(struct.pack('h', int(s * ampr / 2)))
    wav_file.writeframes(struct.pack('h', int(t * ampl / 2)))
    ampr += incr
    ampl -= incl

for s, t in zip(rsound[((len(rsound)//3)*2):], lsound[((len(lsound)//3)*2):]):
    # write the audio frames to file
    wav_file.writeframes(struct.pack('h', int(s * ampr / 2)))
    wav_file.writeframes(struct.pack('h', int(t * ampl / 2)))
    ampr -= incr
