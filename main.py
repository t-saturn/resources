import os
import re

carpeta = "./img/doc"  # tu carpeta

# Patrón en minúsculas y flexible a mayúsculas
patron = re.compile(r"illustration-(\d+)\.png", re.IGNORECASE)

archivos = []
for archivo in os.listdir(carpeta):
    match = patron.match(archivo)
    if match:
        numero = int(match.group(1))
        print(f"Encontrado: {archivo} -> {numero}")  # DEBUG
        if numero >= 59:
            archivos.append((numero, archivo))

print(f"\nTotal encontrados desde 59: {len(archivos)}")

# Ordenar de mayor a menor número
archivos.sort(reverse=True, key=lambda x: x[0])

# Renombrar incrementando en +2
for numero, archivo in archivos:
    nuevo_numero = numero + 2
    nuevo_nombre = f"illustration-{nuevo_numero:03d}.png"
    ruta_vieja = os.path.join(carpeta, archivo)
    ruta_nueva = os.path.join(carpeta, nuevo_nombre)
    os.rename(ruta_vieja, ruta_nueva)
    print(f"Renombrado: {archivo} -> {nuevo_nombre}")
