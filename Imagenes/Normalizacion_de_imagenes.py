import PIL  
from PIL import Image
import os  
import fnmatch  
import tarfile 

print("---->   Normalizacion de imagenes   <----")
dire = input("Ingrese nombre del directorio de imagenes: ")

directorio = './'+dire 
lista_archivos = fnmatch.filter(os.listdir(directorio), '*') 

tamano = input("Ingrese nuevo tamaño: ") 
print("NOTA: Se cambiara a Escala de grises y a al tamaño ingresado")
comprimir = input("¿Tambien desea comprimir estas imagenes? (si/no): ")
os.mkdir("./"+ dire +"_normalizadas") 
os.chmod("./"+ dire +"_normalizadas",777) 

# CAMBIA A ESCALA DE GRISES Y REDIMENSIONA
for x in lista_archivos:
    img = Image.open(x).convert('L')  
    ancho = img.size[0] 
    alto = img.size[1] 
    if ancho > alto:
        base_ancho = int(tamano)
        porcentaje_ancho = (base_ancho /  float(ancho) )
        tam_alto = int(float(alto) * porcentaje_ancho)
        img = img.resize((base_ancho, tam_alto), PIL.Image.ANTIALIAS)
        img.save("./"+ dire +"_normalizadas/" + x)  
        print (x + " ---> OK!") 
 
    else: # SI EL ALTO ES MAYOR QUE EL ANCHO (FOTO VERTICAL) 
        base_alto = int(tamano)
        porcentaje_alto = (base_alto / float(alto))
        tam_ancho = int(float(ancho)  * porcentaje_alto)
        img = img.resize((tam_ancho, base_alto), PIL.Image.ANTIALIAS)
        img.save("./"+ dire +"_normalizadas/" + x) 
        print (x + " ---> OK!") 
 
print("----> Las imagenes se guardaron en "+dire+"_normalizadas")
print ("")

if comprimir == "si" or comprimir == "s":
    
    tar = tarfile.open("./"+ dire +"_normalizadas.tar.gz", "w:gz") 
    tar.add("./"+ dire +"_normalizadas")
    tar.close()
    os.chmod(dire +"_normalizadas.tar.gz",777)
    print ("Fotos comprimidas")
    print("----> El comprimido se guardo en "+dire+"_normalizadas.tar.gz'")
 
print("FIN") 
