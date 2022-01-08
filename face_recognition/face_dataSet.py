import cv2
import numpy as np
import sqlite3
import os

def insertOrUpdate(id, name, age, gender):
    connect = sqlite3.connect("C:/Users/n/Desktop/face/face_recognition/SQLiteStudio/Data.db")

    query = "SELECT * FROM People WHERE ID =" + str(id)
    
    cursor = connect.execute(query)
    
    isRecordExist = 0
    
    for row in cursor:
        isRecordExist = 1
    
    if(isRecordExist == 0):
        query = "Insert into People(ID, Name, Age, Gender) values(" + str(id) + ",'" + str(name) + "','" + str(age) + "','" + str(gender) + "')"
    else:
        query = "Update People set Name = '" + str(name) + "', Age = '"+ str(age) + "', Gender = '" + str(gender) + "' Where ID = '" + str(id)
        
    connect.execute(query)
    connect.commit()
    connect.close()
    
id = input("ID: ")
name = input("Họ tên: ")
age = input("Tuổi: ")
gender = input("Giới tính: ")
insertOrUpdate(id, name, age, gender)
    
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture("C:/test/me.mkv")
numOfImg = 0

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    
    for (x, y, w, h) in faces:  
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        if not os.path.exists('dataSet'):
            os.makedirs('dataSet')

        numOfImg += 1
        cv2.imwrite("dataSet/User." + str(id) + "." + str(numOfImg) + ".jpg", gray[y:y + h, x:x + w])
    cv2.imshow('Detecting face', frame)
    cv2.waitKey(1)
        
    if numOfImg > 100 or (cv2.waitKey(1) & 0xFF == ord('q')):
        break
    
cap.release()
cv2.destroyAllWindows()
    