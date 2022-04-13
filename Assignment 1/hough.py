import cv2
import numpy as np


def detectCircles(img, set_mindist, set_param2):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 
    dp=5, minDist=set_mindist, param2=set_param2, minRadius=250, maxRadius=250)
    if circles is not None:
        # convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")
        # loop over the coordinates and radiuses of the circles
        for (x, y, r) in circles:
            # draw the circle onto the output image
            # and draw a rectangle corresponding to the center of the circle
            cv2.circle(img, (x, y), r, (0, 255, 0), 4)
            cv2.rectangle(img, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
    return img


# select input
capture = cv2.VideoCapture('/Users/marco/Documents/KU Leuven/Computer Vision/Assignment 1/Original Clips/clip6.mp4')

# the following values are returned as floats
width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

# output the captured video onto disk
path = '/Users/marco/Documents/KU Leuven/Computer Vision/Assignment 1/Generated Clips/XXclip6_hough_detection.mp4'
writer = cv2.VideoWriter(path, cv2.VideoWriter_fourcc(*'mp4v'), 20, (width, height))

# set font to add subtitles
font = cv2.FONT_HERSHEY_SIMPLEX

# set starting values for animation
set_param2 = 5
set_mindist = 150

while True:

    ret, frame = capture.read()

    frame = detectCircles(frame, set_mindist, set_param2)
    cv2.putText(frame, text='Circle detection through Hough transform', org=(20, 60), fontFace=font, fontScale=2, color=(255, 255, 255),
        thickness=3, lineType=cv2.LINE_AA)
    cv2.putText(frame, text='tweaking minDist and param2', org=(20, 130), fontFace=font, fontScale=2, color=(255, 255, 255),
        thickness=3, lineType=cv2.LINE_AA)
    if set_param2 < 80:
        set_param2 += 0.5
    if set_mindist < 2000:
        set_mindist += 7
    cv2.imshow('hough', frame)
    writer.write(frame)
    
    # display and write the final transform results
    frame = detectCircles(frame, set_mindist, set_param2)
    cv2.putText(frame, text='Circle detection through Hough transform', org=(20, 60), fontFace=font, fontScale=2, color=(255, 255, 255),
            thickness=3, lineType=cv2.LINE_AA)
    cv2.putText(frame, text='tweaking minDist and param2', org=(20, 130), fontFace=font, fontScale=2, color=(255, 255, 255),
            thickness=3, lineType=cv2.LINE_AA)
    cv2.imshow('hough', frame)
    writer.write(frame)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break

capture.release()
writer.release()
cv2.destroyAllWindows()