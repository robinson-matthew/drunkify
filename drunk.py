import pyaudio
import wave
import time
import cmd, os, sys, signal

class colors:
    """ANSI escape characters that give color to text, bold, underline"""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class DrunkifierApp(cmd.Cmd):
    intro  = "\nThe Drunk Player\n"
    prompt = "Drunkifier > "

    def do_play(self, arg):
        f = arg[0:len(arg)]

        try:
            wf = wave.open(f,'r')
            #wf = wave.open('Roland-JV-2080-Pick-Bass-C2.wav','r')
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
            #byte1 = data[0] 
            #byte2 = data[1] 
            #byte3 = data[2] 
            #byte4 = data[3] 
            
            #data_int = byte1 + byte2 + byte3 + byte4
            #
            #print (data_int)
            
            #print ("Byte-1 Byte-2 Byte-3 Byte-4")
            
            # play stream (looping from beginning of file to the end)
            while len(data) > 0:
                # writing to the stream is what *actually* plays the sound.
                stream.write(data)
                
                data = wf.readframes(int(volume*chunk))  
                if len (data) == 0:
                    break

                #print (len(data))        
                #time.sleep(0.00001)
                #byte1 = data[0] 
                #byte2 = data[1] 
                #byte3 = data[2] 
                #byte4 = data[3] 
            
                #data_int = byte1 + byte2 + byte3 + byte4
            
                #print ("{} {} {} {}".format(byte1,byte2,byte3,byte4))    
             
                #if data[0] >= 100:
                #    data = 0
            
            # cleanup stuff.
            stream.close()    
            p.terminate()
            wf.close()

        except(FileNotFoundError):
            print ("File Not Found")
            pass

    def do_format(self, arg):
        print ("Sample Width: {}".format(wf.getsampwidth()))


    def do_bye(self, arg):
        print ("Bye!")
        sys.exit()


    def do_list(self, arg):
        cwd = os.getcwd()
        cwd_files = os.listdir(cwd)
        print (colors.UNDERLINE + colors.BOLD + colors.OKBLUE,"The Audio Files:",colors.ENDC)
        for i in cwd_files:
            f = i
            f_list = f.split(".")
            if "wav" in f_list:  
                print (colors.OKGREEN,f,colors.ENDC)
            if "mp3" in f_list:  
                print (colors.FAIL,f,colors.ENDC)

    def do_test(self, arg):
        print (arg[0:len(arg)])


def sigint_handler(signum, frame):
    print ("sorry")
    sys.exit()

signal.signal(signal.SIGINT, sigint_handler)


def main():
    DrunkifierApp().cmdloop()

if __name__ == '__main__':
    main()


