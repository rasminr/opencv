import sounddevice as sd
from scipy.io import wavfile
import os as os
import datetime
import time
import numpy as np
import cv2


try:
    os.mkdir("Recording_Mic_without")
except FileExistsError:
    pass

FramesperSec = 44100
RecDur = 0.1
# count = 0
recount = 0
c=0
# photonum=0

cap = cv2.VideoCapture(1)

while c<700:
    recordAudio = sd.rec((int(RecDur * FramesperSec)),samplerate=FramesperSec,channels=2)
    sd.wait()
    wavfile.write(os.path.join("Recording_Mic_without","Recorded_{}.wav".format(recount)),FramesperSec,recordAudio)
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    photoname="./Frame_rec2/"+"frame_"+str(recount)+".jpg"
    # Display the resulting frame
    cv2.imwrite(photoname,gray)
    # photonum=photonum+1
    recount = recount + 1
    # count = count + 1
    c=c+1

cap.release()
cv2.destroyAllWindows()



# cap = cv2.VideoCapture(1)

# photonum=0
# while(True):
#     # Capture frame-by-frame
#     ret, frame = cap.read()

#     # Our operations on the frame come here

#     photoname="./2cam/"+"data"+str(photonum)+".jpg"
#     # Display the resulting frame
#     cv2.imwrite(photoname,frame)
#     photonum=photonum+1
#     if photonum==3:
#         break

# When everything done, release the capture






