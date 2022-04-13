import cv2

# select input
capture = cv2.VideoCapture('/Users/marco/Documents/KU Leuven/Computer Vision/Assignment 1/Original Clips/clip1.mp4') 

# the following values are returned as floats
width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

# output the captured video onto disk
path = '/Users/marco/Documents/KU Leuven/Computer Vision/Assignment 1/Generated Clips/clip1_gaussian_111.mp4'
writer = cv2.VideoWriter(path, cv2.VideoWriter_fourcc(*'mp4v'), 20, (width, height))

# set font to add subtitles
font = cv2.FONT_HERSHEY_SIMPLEX

while True:

    ret, frame = capture.read()
    blurred = cv2.GaussianBlur(frame, (111,111), sigmaX=0)
    cv2.putText(blurred, text='Gaussian blurring, ksize=111', org=(20, 60), fontFace=font, fontScale=2, color=(255, 255, 255),
        thickness=3, lineType=cv2.LINE_AA)
    cv2.putText(blurred, text='isotropic diffusion providing uniform blur', org=(20, 130), fontFace=font, fontScale=2, color=(255, 255, 255),
        thickness=3, lineType=cv2.LINE_AA)
    cv2.putText(blurred, text='non-edge-preserving', org=(20, 200), fontFace=font, fontScale=2, color=(255, 255, 255),
        thickness=3, lineType=cv2.LINE_AA)
    writer.write(blurred)
    cv2.imshow('gaussian blur 111', blurred)

    if cv2.waitKey(1) & 0xFF == 27:
        break

capture.release()
writer.release()
cv2.destroyAllWindows()