import numpy as np 
import cv2 
print("----->Inicia Deteccion de Armas<------")

knive_cascade = cv2.CascadeClassifier('cascade_knives.xml') 
gun_cascade = cv2.CascadeClassifier('cascade_guns.xml') 

img = cv2.imread('prueba.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

knives = knive_cascade.detectMultiScale(gray, 1.1, 15)
guns = gun_cascade.detectMultiScale(gray, 1.1, 15)
bandera=False

for (x, y , w ,h) in knives:
    cv2.rectangle(img, (x,y), (x+w, y+h), (203,224,39), 2)
    bandera=True

for (x, y , w ,h) in guns:
    cv2.rectangle(img, (x,y), (x+w, y+h), (126,30 ,184),2)
    bandera=True
   

if bandera:
    texto = 'Arma' 
    cv2.putText(img, texto, (10,10), cv2.FONT_HERSHEY_PLAIN, 0.9,(0, 0, 255),2)

cv2.imshow('img', img)
cv2.waitKey() 