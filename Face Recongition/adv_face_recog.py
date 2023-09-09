from random import *
import cv2

color = randrange(0, 256)

tr_fc_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
tr_eye_data = cv2.CascadeClassifier('haarcascade_eye.xml')

img = cv2.imread('f_CR7.png')

grsc_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_cords = tr_fc_data.detectMultiScale(grsc_img)

for (x, y, w, h) in face_cords:
    cv2.rectangle(img, (x, y), (x + h, y + w), (color, color, color), 2)

    # roi = region of interest, in this case the roi would be the eyes, which are always on the face
    roi_gray = grsc_img[y:y+h, x:x+w] # will detect where the eyes are in the provided image
    roi_color = img[y:y+h, x:x+w]

    eye_cords = tr_eye_data.detectMultiScale(roi_color) # will get the exact cords of the eyes in the image

    for (ex, ey, ew, eh) in eye_cords:
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (color, color, color), 2)

cv2.imshow('Eye Detection', img)
key = cv2.waitKey()
if key in [81, 113]:
    cv2.destroyAllWindows()
