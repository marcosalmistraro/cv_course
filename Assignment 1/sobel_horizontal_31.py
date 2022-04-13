import cv2
import numpy as np
import skimage.exposure as exposure


def apply_sobel_y(img):
    sobel_y = cv2.Sobel(img, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=31)
    sobel_y = exposure.rescale_intensity(sobel_y, in_range='image', out_range=(0,255)).clip(0,255).astype(np.uint8)
    return sobel_y

# select input
capture = cv2.VideoCapture('/Users/marco/Documents/KU Leuven/Computer Vision/Assignment 1/Original Clips/clip7.mp4')

# the following values are returned as floats
width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

# output the captured video onto disk
path = '/Users/marco/Documents/KU Leuven/Computer Vision/Assignment 1/Generated Clips/clip7_sobel_horizontal_31.mp4'
writer = cv2.VideoWriter(path, cv2.VideoWriter_fourcc(*'mp4v'), 20, (width, height))

# set font to add subtitles
font = cv2.FONT_HERSHEY_SIMPLEX

while True:

    ret, frame = capture.read()
    frame = apply_sobel_y(frame)
    frame = (frame*255).astype(np.uint8) # convert pixels to integer to allow saving output
    cv2.putText(frame, text='Sobel horizontal edge detection, ksize=31', org=(20, 60), fontFace=font, fontScale=2, color=(255, 255, 255),
        thickness=3, lineType=cv2.LINE_AA)
    cv2.imshow('sobel_y', frame)
    writer.write(frame)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break

capture.release()
writer.release()
cv2.destroyAllWindows()