import cv2
import numpy as np


def template_matching(img): 
    img = img.astype(np.uint8)
    template = cv2.imread('/Users/marco/Documents/KU Leuven/Computer Vision/Assignment 1/Original Clips/template.png')
    template = template.astype(np.uint8)
    res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
    return res


# select input
capture = cv2.VideoCapture('/Users/marco/Documents/KU Leuven/Computer Vision/Assignment 1/Original Clips/clip8.mp4')

width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

path = '/Users/marco/Documents/KU Leuven/Computer Vision/Assignment 1/Generated Clips/clip8_template_matching.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
writer = cv2.VideoWriter(path, fourcc, 20, (width, height))

# set font to add subtitles
font = cv2.FONT_HERSHEY_SIMPLEX

while True:

    ret, frame = capture.read()
    frame = template_matching(frame)
    cv2.putText(frame, text='Template matching', org=(900, 450), fontFace=font, fontScale=2, color=(255, 255, 255),
            thickness=3, lineType=cv2.LINE_AA)
    cv2.imshow('template_matching', frame)
    # convert pixels to integer to allow writing file
    frame = (frame*255).astype(np.uint8)
    writer.write(frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

capture.release()
writer.release()
cv2.destroyAllWindows()