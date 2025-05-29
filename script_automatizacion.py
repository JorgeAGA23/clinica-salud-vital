import os
import shutil

carpeta_origen = r"C:\Users\garci\OneDrive\Desktop\SCRIPT BÁSICO (RENOMBRAR ARCHIVOS)"
carpeta_destino = r"C:\Users\garci\OneDrive\Desktop\SCRIPT BÁSICO (RENOMBRAR ARCHIVOS)\archivos_renombrados"

os.makedirs(carpeta_destino, exist_ok=True)

for i, archivo in enumerate(os.listdir(carpeta_origen)):
    ruta_actual = os.path.join(carpeta_origen, archivo)
    if os.path.isfile(ruta_actual):
        _, extension = os.path.splitext(archivo)
        nuevo_nombre = f"archivo_{i+1}{extension}"
        ruta_nueva = os.path.join(carpeta_destino, nuevo_nombre)
        shutil.copy2(ruta_actual, ruta_nueva)
        print(f"Copiado: {archivo} -> {nuevo_nombre}")
