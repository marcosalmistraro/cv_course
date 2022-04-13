import cv2
import numpy as np

# select input
capture = cv2.VideoCapture('/Users/marco/Documents/KU Leuven/Computer Vision/Assignment 1/Original Clips/clip8.mp4')

width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

path = '/Users/marco/Documents/KU Leuven/Computer Vision/Assignment 1/Generated Clips/clip8_template.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
writer = cv2.VideoWriter(path, fourcc, 20, (width, height))

# set font to add subtitles
font = cv2.FONT_HERSHEY_SIMPLEX

while True:

    ret, frame = capture.read()
    cv2.putText(frame, text='Choosing a template over a given frame', org=(20, 60), fontFace=font, fontScale=2, color=(255, 255, 255),
        thickness=3, lineType=cv2.LINE_AA)
    cv2.rectangle(frame, pt1=(1500, 350), pt2=(1600, 450), color=(0, 255, 0), thickness=10)
    cv2.imshow('template', frame)
    writer.write(frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

capture.release()
writer.release()
cv2.destroyAllWindows()