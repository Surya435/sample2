import cv2 as cv
import cv2
cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
    sucess,img =cap.read()
    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0xFF == ord(" "):
        break
cv.imshow('Image',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Black and White',gray)

haar_cascade = cv.CascadeClassifier('face.xml')

face_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=6)


print(f'Number of faces found = {len(face_rect)}')
cv.waitKey(0)&0XFF 