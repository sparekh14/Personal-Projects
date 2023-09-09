from random import *

#################################
# To Run: python face_track.py  #
#################################


import cv2

# load pre-trained face data from the default xml file found on the opencv GitHub
# the CascadeClassifer is a function which can classify cases (through haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# the imread image will read the chosen image into a big array
ch_img = cv2.imread('f_CR7.png')
ch_img2 = cv2.imread('two_ppl.png')

# the image has to be converted to grayscale, as the simple version of the algorithm only deals with grayscale images
# using the grayscale, the algorithm only has to worry about two colors: black and white
grsc_img = cv2.cvtColor(ch_img, cv2.COLOR_BGR2GRAY)
grsc_img2 = cv2.cvtColor(ch_img2, cv2.COLOR_BGR2GRAY)

# the function will detect the face, disregarding the actual scale of the image
# the variable will save the coordinates of where the face is, through which a box can be drawn
face_cords = trained_face_data.detectMultiScale(grsc_img)
print(face_cords) # will return the array [[51 30 81 81]] the first two numbers represent the top left of the face, while the next two reprsent the width and height
face_cords2 = trained_face_data.detectMultiScale(grsc_img2, 10, 1)
print(face_cords2)

# the rectangle function draws a rectangle around the face
# the rectangle function takes in five parameters: the image, (x and y cords of the top left corner), (width and height of the rectangle), (blue, green, red), thickness
for (x, y, w, h) in face_cords2:
    cv2.rectangle(ch_img2, (x, y), (x+h, y+w), (randrange(256), randrange(256), randrange(256)), 1)

# displays the image
cv2.imshow('Face Tracking Image', ch_img2)

# pauses the code, and will continue to display the image, until a key is pressed
# once a key is pressed, the image will automatically close
cv2.waitKey()

print('Hello, World!')
