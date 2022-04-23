import os
import cv2 as cv
import numpy as np


people = ['Joe Biden', 'Vladimir Putin', 'Donald Trump']
DIR = r'C:\Users\zangi\Programmering\Images for lab 6.2 script\img\training'
haar_cascade = cv.CascadeClassifier('haar_face.xml')


def train_faces():
    features = []
    labels = []
    
    print('Loading every image into training')
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)
        
        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            
            img_array = cv.imread(img_path)
            print(f'Training image at {img_path}')
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=2, minNeighbors=4)
            
            for(x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)    
    
    features = np.array(features, dtype='object')
    labels = np.array(labels)

    face_recognizer = cv.face.LBPHFaceRecognizer_create()
    face_recognizer.train(features, labels)
    
    face_recognizer.save('face_trained.yml')
    np.save('features.npy', features)
    np.save('labels.npy', labels)

    
def recognize_faces(img_path):
    face_recognizer = cv.face.LBPHFaceRecognizer_create()
    face_recognizer.read('face_trained.yml')
    
    img = cv.imread(img_path)
    
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # cv.imshow('Person', gray)
    
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
    
    for (x,y,w,h) in faces_rect:
        faces_roi = gray[y:y+h,x:x+h]
        label, confidence = face_recognizer.predict(faces_roi)
        print(f'Label = {people[label]} with a confidence of {confidence}')
    
        image = cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)
        cv.putText(image, f'{str(people[label])} {confidence}', (x, y-10), cv.FONT_HERSHEY_COMPLEX, 0.75, (0,255,0), thickness=2)
    
    cv.imshow('Detected face', img)
    cv.waitKey(0)