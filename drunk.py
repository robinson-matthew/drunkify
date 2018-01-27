import pyaudio
import wave
import time

#wf = wave.open('tesfile2.wav','r')
wf = wave.open('4-Laurence_Guy_-_Rizzo.wav','r')
p = pyaudio.PyAudio()

chunk = 1
volume = 1


# open stream based on the wave object which has been input.
stream = p.open(format =
                p.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(),
                rate = wf.getframerate(),
                output = True)

# read data (based on the chunk size)
data = wf.readframes(chunk)

# play stream (looping from beginning of file to the end)
while data != 0:
    # writing to the stream is what *actually* plays the sound.
    stream.write(data)
    
    data = wf.readframes(int(volume*chunk))  
    #time.sleep(0.00001)
    #print (data[0])
    #if data[0] >= 100:
    #    data = 0

# cleanup stuff.
stream.close()    
p.terminate()


print ('python is not sad')


wf.close()
