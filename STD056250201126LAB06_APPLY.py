import cv2
import os
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +
                'haarcascade_frontalface_default.xml')
video = cv2.VideoCapture(0)
try :
    os.mkdir('natthanon')

except:
    print("U HAVE myFace")
try:
    os.mkdir('mask')

except:
    print("U HAVE mask")
try:
    os.mkdir('nomask')

except:
    print("U HAVE nomask")
try:
    os.mkdir('sad')

except:
    print("U HAVE sad")

try:
    os.mkdir('happy')

except:
    print("U HAVE happy")
try:
    os.mkdir('angry')
except:
    print("U HAVE angry")

i = 0 #my self
j = 0 #mask
k = 0 #no mask
l = 0 #sad
u = 0 #happy
o = 0 #angry
while True:
    ret, frame = video.read()
    faces = face_cascade.detectMultiScale(frame,
            scaleFactor=1.1, minNeighbors=5)
    for x,y,w,h in faces:
        roi_color = frame[y+3:y + h-3,
        x+3:x + w-3]
        frame = cv2.rectangle(frame,
                (x,y), (x+w,y+h),
                (0,255,0), 3)
        cv2.putText(frame, "human", (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    2, (0, 0, 255), 5)
    cv2.putText(frame, 'c = myself', (50, 50), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 0), 1)
    cv2.putText(frame, 'm = mask', (50, 80), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 0, 0), 1)
    cv2.putText(frame, 'n = no mask', (50, 110), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 0, 0), 1)
    cv2.putText(frame, 's = sad', (50, 140), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 0, 0), 1)
    cv2.putText(frame, 'h = happy', (50, 170), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 0, 0), 1)
    cv2.putText(frame, 'a = angry', (50, 200), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 0, 0), 1)
    cv2.imshow('Face Detector', frame)


    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('c'): #myself
        os.chdir('C:/IMAGEproject/natthanon')
        imgname = 'natthanon' + str(i) + '.jpg'
        cv2.imwrite(imgname, roi_color)
        print('Save: %s', imgname)
        i += 1
    elif key == ord('m'): #mask
        os.chdir('C:/IMAGEproject/mask')
        imgname = 'mask' + str(j) + '.jpg'
        cv2.imwrite(imgname, roi_color)
        print('Save: %s', imgname)
        j += 1
    elif key == ord('n'): #no mask
        os.chdir('C:/IMAGEproject/nomask')
        imgname = 'nomask' + str(k) + '.jpg'
        cv2.imwrite(imgname, roi_color)
        print('Save: %s', imgname)
        k += 1
    elif key == ord('s'): #sad
        os.chdir('C:/IMAGEproject/sad')
        imgname = 'sad' + str(l) + '.jpg'
        cv2.imwrite(imgname, roi_color)
        print('Save: %s', imgname)
        l += 1
    elif key == ord('h'): #happy
        os.chdir('C:/IMAGEproject/happy')
        imgname = 'happy' + str(u) + '.jpg'
        cv2.imwrite(imgname, roi_color)
        print('Save: %s', imgname)
        u += 1
    elif key == ord('a'): #angry
        os.chdir('C:/IMAGEproject/angry')
        imgname = 'angry' + str(o) + '.jpg'
        cv2.imwrite(imgname, roi_color)
        print('Save: %s', imgname)
        o += 1

video.release()
cv2.destroyAllWindows()
