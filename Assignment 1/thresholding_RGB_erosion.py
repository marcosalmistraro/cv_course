import cv2
import numpy as np


def erode(img, kernel_size):
    kernel = np.ones((kernel_size, kernel_size), dtype=np.uint8)
    eroded = cv2.erode(img, kernel, iterations=1)
    return eroded


# select input
capture = cv2.VideoCapture('/Users/marco/Documents/KU Leuven/Computer Vision/Assignment 1/Original Clips/clip5.mp4')

# the following values are returned as floats
width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

# output the captured video onto disk
path = '/Users/marco/Documents/KU Leuven/Computer Vision/Assignment 1/Generated Clips/clip5_thresh_RGB_erosion.mp4'
writer = cv2.VideoWriter(path, cv2.VideoWriter_fourcc(*'mp4v'), 20, (width, height))

# set font to add subtitles
font = cv2.FONT_HERSHEY_SIMPLEX

while True:

    ret, frame = capture.read()

    # apply binary threshold
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    ret1, thresh1 = cv2.threshold(src=gray, thresh=127, maxval=255, type=cv2.THRESH_BINARY)

    # apply a morphological operator to the thresholded image
    eroded_img = erode(thresh1, 30)
    
    # compute difference between the images
    diff = cv2.absdiff(eroded_img, thresh1)
    
    # generate blended image accounting for both operations
    thresh1 = cv2.cvtColor(thresh1, cv2.COLOR_GRAY2BGR)
    diff = cv2.cvtColor(diff, cv2.COLOR_GRAY2BGR)
    diff[np.where((diff==[255, 255, 255]).all(axis=2))] = [0, 255, 0]
    blended = cv2.addWeighted(src1=thresh1, alpha=0.8, src2=diff, beta=2, gamma=0)

    # display and write the blended image
    cv2.putText(blended, text='Erosion morphological operator, kernel_size=30', org=(20, 60), fontFace=font, fontScale=2, color=(255, 255, 255),
        thickness=3, lineType=cv2.LINE_AA)
    cv2.imshow('blended', blended)
    writer.write(blended)

    if cv2.waitKey(1) & 0xFF == 27:
        break

capture.release()
writer.release()
cv2.destroyAllWindows()