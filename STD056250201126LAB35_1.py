import cv2
image = cv2.imread('humanface2.png')
#image = cv2.imread('test01.jpg')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
detectface = detector.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=3,minSize=(30, 30))


for idx,(x, y, w, h,) in enumerate(detectface):

    print((x, y, w, h,))
    cv2.rectangle(image, (x, y),(x + w, y + h),(0, 255, 0), 1)


    cv2.putText(image,str(idx+1) ,(x,y),cv2.FONT_HERSHEY_SIMPLEX,1, (0, 0, 255), 2 )
    print(idx+1)
    crop_img = image[y:y + h, x:x + w]
    cv2.imwrite("STD056250201126lab35_1.jpg", image)
    cv2.imwrite('person' + str(idx + 1) + '.jpg', crop_img)
    #cv2.imwrite('Human' + str(idx+1) + '.jpg', crop_img)

cv2.imshow('Test Face',image)
cv2.waitKey(0)