import cv2
import numpy as np
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# img = cv2.imread("C:/Users/Admin/.vscode/Python/test2.jpg")
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cap = cv2.VideoCapture("C:/test/me.mkv")

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    print(frame)
    for (x, y, w, h) in faces:  
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow('Detecting face', frame)
    
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break
cap.release() 
cv2.destroyAllWindows()