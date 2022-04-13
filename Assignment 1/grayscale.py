import cv2

# select input
capture = cv2.VideoCapture('/Users/marco/Documents/KU Leuven/Computer Vision/Assignment 1/Original Clips/clip3.mp4')

# the following values are returned as floats
width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

# output the captured video onto disk
path = '/Users/marco/Documents/KU Leuven/Computer Vision/Assignment 1/Generated Clips/clip3_grayscale.mp4'
writer = cv2.VideoWriter(path, cv2.VideoWriter_fourcc(*'mp4v'), 20, (width, height), isColor=False)

# set font to add subtitles
font = cv2.FONT_HERSHEY_SIMPLEX

while True:

    ret, frame = capture.read()
    # convert frame to grayscalew
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.putText(frame, text='Grayscale image', org=(20, 60), fontFace=font, fontScale=2, color=(255, 255, 255),
            thickness=3, lineType=cv2.LINE_AA)
    writer.write(frame)
    cv2.imshow('grayscale', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

capture.release()
writer.release()
cv2.destroyAllWindows()