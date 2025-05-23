"""Convert Video2JPG
"""

import cv2
import os
import imutils
# Read the video from specified path
cam = cv2.VideoCapture("Path/vid-wheels.mp4")

try:

    # creating a folder named data
    if not os.path.exists('Path/vid-wheels'):
        os.makedirs('Path/vid-wheels')

# if not created then raise error
except OSError:
    print ('Error: Creating directory of data')

# frame
currentframe = 0

while(True):

    # reading from frame
    ret,frame = cam.read()

    if ret:
        # if video is still left continue creating images
        name = 'Path/vid-wheels/frame' + str(currentframe) + '.jpg'
        print ('Creating...' + name)
        rot = imutils.rotate(frame, angle=-90)
        # writing the extracted images
        cv2.imwrite(name, rot)

        # increasing counter so that it will
        # show how many frames are created
        currentframe += 1
    else:
        break

# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()