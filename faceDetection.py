import cv2

image = cv2.imread('humanface2.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

detector = cv2.CascadeClassifier(cv2.data.haarcascades +
                                 "haarcascade_frontalface_default.xml")
detectface = detector.detectMultiScale(
    gray,
    scaleFactor=1.3,
    minNeighbors=3,
    minSize=(30, 30)
  )

for (x, y, w, h) in detectface:
    cv2.rectangle(image, (x, y),
                  (x + w, y + h),
                  (0, 255, 0), 2)

cv2.imshow('Test Face' ,image)
cv2.waitKey(0)