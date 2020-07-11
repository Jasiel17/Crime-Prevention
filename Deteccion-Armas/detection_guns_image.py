import numpy as np 
import cv2 

gun_cascade = cv2.CascadeClassifier('cascade_guns.xml') 
img = cv2.imread('tg3.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
guns = gun_cascade.detectMultiScale(gray, 1.1, 9) # 1:1 cuánto se reduce el tamaño de la imagen en cada escala de imagen, 
#cuántos vecinos debe tener cada rectángulo candidato para retenerlo
for (x, y , w ,h) in guns:
    cv2.rectangle(img, (x,y), (x+w, y+h), (126,30 ,184),2)
    texto = 'Arma de Fuego' 
    cv2.putText(img, texto, (10,10), cv2.FONT_HERSHEY_PLAIN, 0.9,(0, 0, 255),1)
#imagen, coor ini,coor fin, color,grosor linea

cv2.imshow('img', img)
cv2.waitKey() 
