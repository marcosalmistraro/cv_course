import cv2

# select input
capture = cv2.VideoCapture('/Users/marco/Documents/KU Leuven/Computer Vision/Assignment 1/Original Clips/clip5.mp4')

# the following values are returned as floats
width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
 
# output the captured video onto disk
path = '/Users/marco/Documents/KU Leuven/Computer Vision/Assignment 1/Generated Clips/clip5_thresholded_RGB.mp4'
writer = cv2.VideoWriter(path, cv2.VideoWriter_fourcc(*'mp4v'), 20, (width, height), isColor=False)

# set font to add subtitles
font = cv2.FONT_HERSHEY_SIMPLEX

while True:

    ret, frame = capture.read()
    # apply binary threshold to greyscale image
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    ret1, thresh = cv2.threshold(src=gray, thresh=127, maxval=255, type=cv2.THRESH_BINARY)

    # display and save the thresholded image
    cv2.putText(thresh, text='Thresholded image, thresh=127', org=(20, 60), fontFace=font, fontScale=2, color=(255, 255, 255),
            thickness=3, lineType=cv2.LINE_AA)
    cv2.putText(thresh, text='object grabbing in RGB space', org=(20, 130), fontFace=font, fontScale=2, color=(255, 255, 255),
            thickness=3, lineType=cv2.LINE_AA)
    writer.write(thresh)
    cv2.imshow('thresh', thresh)

    if cv2.waitKey(1) & 0xFF == 27:
        break

capture.release()
writer.release()
cv2.destroyAllWindows()