import cv2
import os
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
video = cv2.VideoCapture(0)
os.mkdir('myface')
i = 0
while True:
    ret, frame = video.read()
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5)

    for x,y,w,h in faces:
        roi_color = frame[y+3:y + h-3, x+3:x + w-3]
        frame = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)

    cv2.imshow('Face Detector', frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

    elif key == ord('c'):
        imgname = 'C:\IMAGEproject\LAB6\myface\myname' + str(i) + '.jpg'
        cv2.imwrite(imgname, roi_color)
        print('Save: %s', imgname)
        i += 1

video.release()
cv2.destroyAllWindows()