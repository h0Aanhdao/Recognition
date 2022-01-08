import cv2
import numpy as np
import sqlite3
from PIL import Image

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.read('recognizer/trainingData.yml')

def getProfile(id):
    connect = sqlite3.connect('C:/Users/n/Desktop/face/face_recognition/SQLiteStudio/Data.db')
    query = "SELECT * FROM People WHERE ID =" + str(id)
    cursor = connect.execute(query)
    profile = None
    for row in cursor:
        profile = row
    connect.close()
    return profile
cap = cv2.VideoCapture("C:/test/headphone.mkv")

font = cv2.FONT_HERSHEY_SIMPLEX

i = 0;
total = 0.0;
ave = 0.0;
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    
    for (x, y, w, h) in faces:  
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        grayImg = gray[y: y + h, x: x + h]
        
        id, confidence = recognizer.predict(grayImg)
        confidence=100*(1-(confidence)/300)
        if(confidence > 70):
            i+=1;
            total += confidence;
            ave = total / i;
            print("So lan: ", i);
            print("Trung binh: ", ave);
            profile = getProfile(id)
            if(profile != None):
                cv2.putText(frame, "Name: " + str(profile[1]), (x + 10, y + h + 30), font, 0.8, (0, 255, 0), 2)
                cv2.putText(frame, "Age: " + str(profile[2]), (x + 10, y + h + 60), font, 0.8, (0, 255, 0), 2)
                cv2.putText(frame, "Gender: " + str(profile[3]), (x + 10, y + h + 90), font, 0.8, (0, 255, 0), 2)
                cv2.putText(frame, "Confidence: " + "{:.5f}".format(confidence), (x + 10, y + h + 120), font, 0.8, (0, 255, 2), 2)
        else:
            cv2.putText(frame, "Unknown", (x + 10, y + h + 30), font, 0.8, (0, 255, 0), 2)
        
    cv2.imshow("Image",frame)
    
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break
    
cap.release() 
cv2.destroyAllWindows()