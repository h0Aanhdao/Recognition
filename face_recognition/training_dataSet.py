import cv2
import numpy as np
import os
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
path = 'dataSet'


def getImagePath(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    print(imagePaths)

    faces = []
    IDs = []
    
    for imagePath in imagePaths:
        print(imagePath)
        faceImg = Image.open(imagePath).convert('L')
        faceNp = np.array(faceImg, 'uint8')
        # print(imagePath.split('\\')[1].split('.')[1])
        ID = int(imagePath.split('\\')[1].split('.')[1])
        # print(faceNp)
        faces.append(faceNp)
        IDs.append(ID)
        
        # cv2.imshow('Training', faceNp)
        cv2.waitKey(1)
        
    return faces,IDs
    
faces,IDs = getImagePath(path)

    # Training
recognizer.train(faces,np.array(IDs))
print("Faces", recognizer)

if not os.path.exists('recognizer'):
    os.makedirs('recognizer')
recognizer.save('recognizer/trainingData.yml')
cv2.destroyAllWindows()
    