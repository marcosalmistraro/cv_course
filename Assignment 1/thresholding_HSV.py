import cv2
import numpy as np

# select input
capture = cv2.VideoCapture('/Users/marco/Documents/KU Leuven/Computer Vision/Assignment 1/Original Clips/clip5.mp4')

# the following values are returned as floats
width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

# output the captured video onto disk
path = '/Users/marco/Documents/KU Leuven/Computer Vision/Assignment 1/Generated Clips/clip5_thresholded_HSV.mp4'
writer = cv2.VideoWriter(path, cv2.VideoWriter_fourcc(*'mp4v'), 20, (width, height))

# set font to add subtitles
font = cv2.FONT_HERSHEY_SIMPLEX

while True:

    ret, frame = capture.read()
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # set lower and upper boundaries for thresholding
    lower = np.array([0, 0, 0], dtype="uint8")
    upper = np.array([60, 200, 200], dtype="uint8")
    hsv = cv2.inRange(hsv, lower, upper)
    hsv = cv2.bitwise_not(hsv)

    cv2.putText(hsv, text='Object grabbing', org=(800, 450), fontFace=font, fontScale=2, color=(0, 220, 255),
            thickness=3, lineType=cv2.LINE_AA)
    cv2.putText(hsv, text='in HSV space', org=(800, 520), fontFace=font, fontScale=2, color=(0, 220, 255),
            thickness=3, lineType=cv2.LINE_AA)
        
    cv2.imshow('hsv', hsv) 
    writer.write(hsv)

    if cv2.waitKey(1) & 0xFF == 27:
        break

capture.release()
writer.release()
cv2.destroyAllWindows()