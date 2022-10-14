import cv2
from random import *

color = randrange(0, 256)

tr_fc_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
tr_sm_data = cv2.CascadeClassifier('haarcascade_smile.xml')

# to capture video from the webcam
webcam = cv2.VideoCapture(0)  # the 0, will set the webcam to the default webcam, and a specific video file can also be mentioned

while True:  # run a loop through all the frames in the video/webcam until the video/webcam ends or the we kill it
    successful_frame_read, frame = webcam.read()  # returns a tuple: (a bool showing whether the frame read was succesful and should always be True, the frame of the video which is being read)

    grsc_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # convert the frame to a grayscale

    faces = tr_fc_data.detectMultiScale(grsc_img, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + h, y + w), (color, color, color), 4)

        face = frame[y:y+h, x:x+h]

        face_grsc = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

        smile = tr_sm_data.detectMultiScale(face_grsc, 1.7, 20)

        for (x_, y_, w_, h_) in faces:
            cv2.rectangle(face, (x_, y_), (x_+ w_, y_+h_), (color, color, color), 4)

        if len(smile) > 0:
            cv2.putText(frame, 'smiling', (x+50, y+200), fontScale=1, fontFace=cv2.FONT_HERSHEY_TRIPLEX, color=(color, color, color))

    cv2.imshow('Video Tracking Image', frame)

    key = cv2.waitKey(1)  # waits for 1 millisecond and it will autohit a key, so the video is continuous, the key variable also captures the key pressed

    # stops the webcam when either 'q' or 'Q' is pressed, using their ASCII values
    if key in [81, 113]:
        break

print('Hello, World!!!')
