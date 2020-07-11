import numpy as np 
import cv2 
import imutils 
import datetime 

gun_cascade = cv2.CascadeClassifier('cascade_guns.xml') 
knive_cascade = cv2.CascadeClassifier('cascade_Knives.xml') 

camera = cv2.VideoCapture('video.mp4') 
firstFrame = None

gun_exist = False
knive_exist = False

while True: 
      
    ret, frame = camera.read() 
    frame = imutils.resize(frame, width = 500) 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
       
    gun = gun_cascade.detectMultiScale(gray,  1.3, 8, minSize = (100, 100)) 
    knive = knive_cascade.detectMultiScale(gray, 1.3, 15, minSize = (100, 100)) 
       
    if len(gun) > 0: 
        gun_exist = True

    if len(knive) > 0: 
        knive_exist = True
           
    for (x, y, w, h) in gun: 
          
        frame = cv2.rectangle(frame, 
                              (x, y), 
                              (x + w, y + h), 
                              (126,30 ,184), 3) 
        roi_gray = gray[y:y + h, x:x + w] 
        roi_color = frame[y:y + h, x:x + w]     
    
           
    for (x, y, w, h) in knive: 
          
        frame = cv2.rectangle(frame, 
                              (x, y), 
                              (x + w, y + h), 
                              (203,224,39), 3) 
        roi_gray = gray[y:y + h, x:x + w] 
        roi_color = frame[y:y + h, x:x + w] 

    if firstFrame is None: 
        firstFrame = gray 
        continue
   
    
    # fecha
    cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S %p"), 
                (10, frame.shape[0] - 10), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.35, (0, 0, 3), 1) 
   
    cv2.imshow("Security Feed", frame) 
    key = cv2.waitKey(1) & 0xFF
      
    if key == ord('q'): 
        break
  


camera.release() 
cv2.destroyAllWindows() 