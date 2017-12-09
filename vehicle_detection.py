# -*- coding: utf-8 -*-

import cv2
from firebase import firebase
print(cv2.__version__)

cascade_src = 'cars.xml'
#video_src = 'dataset/video1.avi'
#video_src = 'dataset/video2.avi'
count=0
cap = cv2.VideoCapture(0)
car_cascade = cv2.CascadeClassifier(cascade_src)

import requests
r = requests.get('https://api.ipdata.co').json()

while True:
    ret, img = cap.read()
    if (type(img) == type(None)):
        break
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)

    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        count=count+1
        
    cv2.imshow('video', img)
    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()
FIREBASE_URL = "https://iot3-27a0b.firebaseio.com/"
fb = firebase.FirebaseApplication(FIREBASE_URL, None)
data = str(count)+'-GPS_DETAILS_COUNTRY-'+r['country_name']+'-LATITUDE-'+str(r['latitude'])+'-LONGITUDE-'+str(r['longitude'])
fb.put('FirebaseDB_Demo', "Data", data)
print('FirebaseDB_Demo', "Data", data)
