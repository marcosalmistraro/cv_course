import cv2

# select input
capture = cv2.VideoCapture('/Users/marco/Documents/KU Leuven/Computer Vision/Assignment 1/Original Clips/clip1.mp4')

# the following values are returned as floats
width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

# output the captured video onto disk
path = '/Users/marco/Documents/KU Leuven/Computer Vision/Assignment 1/Generated Clips/clip1_bilateral.mp4'
writer = cv2.VideoWriter(path, cv2.VideoWriter_fourcc(*'mp4v'), 20, (width, height))

# set font to add subtitles
font = cv2.FONT_HERSHEY_SIMPLEX

while True:

    ret, frame = capture.read()
    # apply bilateral filter to current frame
    bilateral = cv2.bilateralFilter(frame, d=10, sigmaColor=300, sigmaSpace=300)
    # add subtitles to current frame
    cv2.putText(bilateral, text='Bilateral filtering, sigmaColor=300, sigmaSpace=300', org=(20, 60), fontFace=font, fontScale=2, color=(255, 255, 255),
            thickness=3, lineType=cv2.LINE_AA)
    cv2.putText(bilateral, text='two Gaussian filters, for both space and color', org=(20, 130), fontFace=font, fontScale=2, color=(255, 255, 255),
        thickness=3, lineType=cv2.LINE_AA)
    cv2.putText(bilateral, text='edge-preserving', org=(20, 200), fontFace=font, fontScale=2, color=(255, 255, 255),
        thickness=3, lineType=cv2.LINE_AA)
    writer.write(bilateral)
    cv2.imshow('bilateral', bilateral)

    if cv2.waitKey(1) & 0xFF == 27:
        break

capture.release()
writer.release()
cv2.destroyAllWindows()