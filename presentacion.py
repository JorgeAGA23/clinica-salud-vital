import os
carpeta = r"C:\Users\garci\OneDrive\Desktop\archivos"
for i, archivo in enumerate(os.listdir(carpeta)):
    _, extension = os.path.splitext(archivo)
    nuevo = f"archivo_{i+1}{extension}"
    os.rename(os.path.join(carpeta, archivo), os.path.join(carpeta, nuevo))





#Apagar la PC
import os
os.system("shutdown /s /t 10")

#Hacer respaldo
import shutil
shutil.copy("archivo.txt", "respaldo/")

