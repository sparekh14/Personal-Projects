from random import *
import cv2

class Videos():

    def webc(self):
        color = randrange(0, 256)

        tr_fc_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        # to capture video from the webcam
        webcam = cv2.VideoCapture(0)  # the 0, will set the webcam to the default webcam, and a specific video file can also be mentioned

        while True:  # run a loop through all the frames in the video/webcam until the video/webcam ends or the we kill it
            successful_frame_read, frame = webcam.read()  # returns a tuple: (a bool showing whether the frame read was succesful and should always be True, the frame of the video which is being read)
            grsc_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # convert the frame to a grayscale
            face_cords = tr_fc_data.detectMultiScale(grsc_img)
            for (x, y, w, h) in face_cords:
                cv2.rectangle(frame, (x, y), (x + h, y + w), (color, color, color), 3)
            cv2.imshow('Video Tracking Image', frame)
            key = cv2.waitKey(1)  # waits for 1 millisecond and it will autohit a key, so the video is continuous, the key variable also captures the key pressed
            # stops the webcam when either 'q' or 'Q' is pressed, using their ASCII values
            if key in [81, 113]:
                break

    def video(self):
        color = randrange(0, 256)

        tr_fc_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        # to capture video from the webcam
        webcam = cv2.VideoCapture('test_video.mp4')  # the 0, will set the webcam to the default webcam, and a specific video file can also be mentioned

        while True:  # run a loop through all the frames in the video/webcam until the video/webcam ends or the we kill it
            successful_frame_read, frame = webcam.read()  # returns a tuple: (a bool showing whether the frame read was succesful and should always be True, the frame of the video which is being read)
            grsc_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # convert the frame to a grayscale
            face_cords = tr_fc_data.detectMultiScale(grsc_img)
            for (x, y, w, h) in face_cords:
                cv2.rectangle(frame, (x, y), (x + h, y + w), (color, color, color), 3)
            cv2.imshow('Video Tracking Image', frame)
            key = cv2.waitKey(
                1)  # waits for 1 millisecond and it will autohit a key, so the video is continuous, the key variable also captures the key pressed
            # stops the webcam when either 'q' or 'Q' is pressed, using their ASCII values
            if key in [81, 113]:
                break

    def eyes(self):
        color = randrange(0, 256)

        tr_fc_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        tr_eye_data = cv2.CascadeClassifier('haarcascade_eye.xml')

        webcam = cv2.VideoCapture(0)

        while True:
            successful_frame_read, frame = webcam.read()

            grsc_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            face_cords = tr_fc_data.detectMultiScale(grsc_img)

            for (x, y, w, h) in face_cords:
                cv2.rectangle(frame, (x, y), (x + h, y + w), (color, color, color), 2)

                # roi = region of interest, in this case the roi would be the eyes, which are always on the face
                roi_gray = grsc_img[y:y + h, x:x + w]
                roi_color = frame[y:y + h, x:x + w]

                eye_cords = tr_eye_data.detectMultiScale(roi_color)  # will get the exact cords of the eyes in the image

                for (ex, ey, ew, eh) in eye_cords:
                    cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (color, color, color), 2)

            key = cv2.waitKey(1)
            if key in [81, 113]:
                break
