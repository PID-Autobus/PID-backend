import os

def encontrar_txt_sin_imagenes(imagenes_folder):
    imagenes = set()
    txt_sin_imagen = []

    for filename in os.listdir(imagenes_folder):
        base_name, extension = os.path.splitext(filename)

        if extension.lower() == ".jpg" or extension.lower() == ".png":
            imagenes.add(base_name)
        elif extension.lower() == ".txt":
            txt_sin_imagen.append(base_name)

    txt_sin_imagen = set(txt_sin_imagen)
    txt_sin_imagen = txt_sin_imagen.difference(imagenes)

    return list(txt_sin_imagen)

# Ejemplo de uso para encontrar archivos .txt sin imágenes correspondientes
imagenes_folder = 'C:/Users/Josemari/Desktop/Images_RGB'
archivos_sin_imagen = encontrar_txt_sin_imagenes(imagenes_folder)

if archivos_sin_imagen:
    print("Archivos .txt sin imágenes correspondientes:")
    for archivo in archivos_sin_imagen:
        print(f"- {archivo}.txt")
else:
    print("Todos los archivos .txt tienen imágenes correspondientes.")
