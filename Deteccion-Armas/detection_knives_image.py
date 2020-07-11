import numpy as np 
import cv2 
print("Inicia Deteccion de Armas")

knive_cascade = cv2.CascadeClassifier('cascade_knives.xml')  
img = cv2.imread('pel2.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
knives = knive_cascade.detectMultiScale(gray, 1.1, 9)

for (x, y , w ,h) in knives:
    cv2.rectangle(img, (x,y), (x+w, y+h), (203,224,39), 3)
    texto = 'Arma Blanca' 
    cv2.putText(img, texto, (10,10), cv2.FONT_HERSHEY_PLAIN, 0.9,(255, 0, 0),2)

cv2.imshow('img', img)
cv2.waitKey() 
