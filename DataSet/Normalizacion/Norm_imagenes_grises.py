import PIL  
from PIL import Image
import os  
import fnmatch  
import tarfile 

print("---->   Normalizacion de imagenes   <----")
dire = input("Ingrese nombre del directorio de imagenes: ")

current_dir = os.path.dirname(os.path.abspath(__file__))
directorio = os.path.join(current_dir,dire)
lista_archivos = fnmatch.filter(os.listdir(directorio), '*') 

os.mkdir(directorio+"_norm") 
os.chmod(directorio+"_norm",777) 
tamano = input("Ingrese nuevo tamaño: ") 
print("NOTA: Se cambiara a Escala de grises y al tamaño ingresado")
comprimir = input("¿Tambien desea comprimir estas imagenes? (si/no): ")

dirb = directorio+"_norm/"
# CAMBIA A ESCALA DE GRISES Y REDIMENSIONA
for x in lista_archivos:
    img = Image.open(directorio+"/"+x).convert('L')  
    ancho = img.size[0] 
    alto = img.size[1] 
    if ancho > alto:
        base_ancho = int(tamano)
        porcentaje_ancho = (base_ancho /  float(ancho) )
        tam_alto = int(float(alto) * porcentaje_ancho)
        img = img.resize((base_ancho, tam_alto), PIL.Image.ANTIALIAS)
        img.save(dirb+x)  
        print (x + " ---> OK!") 
 
    else: # SI EL ALTO ES MAYOR QUE EL ANCHO (FOTO VERTICAL) 
        base_alto = int(tamano)
        porcentaje_alto = (base_alto / float(alto))
        tam_ancho = int(float(ancho)  * porcentaje_alto)
        img = img.resize((tam_ancho, base_alto), PIL.Image.ANTIALIAS)
        img.save(dirb+x) 
        print (x + " ---> OK!") 
 
print("----> Las imagenes se guardaron en "+dire+"_norm")
print ("")

if comprimir == "si" or comprimir == "s":
    
    tar = tarfile.open("./"+ dire +"_norm.tar.gz", "w:gz") 
    tar.add("./"+ dire +"_norm")
    tar.close()
    os.chmod(dire +"_norm.tar.gz",777)
    print ("Fotos comprimidas")
    print("----> El comprimido se guardo en "+dire+"_norm.tar.gz'")
 
print("FIN") 
