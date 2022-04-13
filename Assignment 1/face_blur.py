import cv2


def detect_and_blur_face(img):
    face_img = img.copy()
    face_rects = face_cascade.detectMultiScale(face_img, scaleFactor=1.2, minNeighbors=5)
    for (x, y, w, h) in face_rects:
        roi = face_img[y:y+h, x:x+w, :]
        roi = cv2.medianBlur(roi, 55)
        face_img[y:y+h, x:x+w, :] = roi
    return face_img


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# select input
cap = cv2.VideoCapture(0) 

# the following values are returned as floats
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# output the captured video onto disk
path = '/Users/marco/Documents/KU Leuven/Computer Vision/Assignment 1/Generated Clips/face_blurring.mp4'
writer = cv2.VideoWriter(path, cv2.VideoWriter_fourcc(*'mp4v'), 15, (width, height))

# set font to add subtitles
font = cv2.FONT_HERSHEY_SIMPLEX

while True:

    ret, frame = cap.read(0)
    frame = detect_and_blur_face(frame)
    cv2.putText(frame, text='Face blurring using Haar cascades', org=(20, 60), fontFace=font, fontScale=2, color=(255, 255, 255),
        thickness=3, lineType=cv2.LINE_AA)
    cv2.imshow('Face blurring', frame)
    writer.write(frame)
    
    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()