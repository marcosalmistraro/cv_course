import cv2
import numpy as np


def edge_mask(img, line_size, blur_value):
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  gray_blur = cv2.medianBlur(gray, blur_value)
  edges = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, line_size, blur_value)
  return edges


# values for edge mask
line_size = 7
blur_value = 7

# select input from webcam
capture = cv2.VideoCapture(0)

# the following values are returned as floats
width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

# output the captured video onto disk
path = '/Users/marco/Documents/KU Leuven/Computer Vision/Assignment 1/Generated Clips/cartoon_effect.mp4'
writer = cv2.VideoWriter(path, cv2.VideoWriter_fourcc(*'mp4v'), 15, (width, height), isColor=False)

# set font to add subtitles
font = cv2.FONT_HERSHEY_SIMPLEX

while True:

    ret, frame = capture.read()
    edges = edge_mask(frame, line_size, blur_value)
    cv2.putText(edges, text='Cartoon effect', org=(20, 60), fontFace=font, fontScale=2, color=(0, 0, 0),
            thickness=3, lineType=cv2.LINE_AA)
    cv2.imshow('cartoon', np.uint8(edges))
    writer.write(edges)

    if cv2.waitKey(1) & 0xFF == 27:
        break

capture.release()
writer.release()
cv2.destroyAllWindows()