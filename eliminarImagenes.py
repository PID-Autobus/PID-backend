import os

def eliminar_txt_sin_imagenes(imagenes_folder):
    for filename in os.listdir(imagenes_folder):
        if filename.endswith(".txt"):
            txt_path = os.path.join(imagenes_folder, filename)
            imagen_path = os.path.join(imagenes_folder, os.path.splitext(filename)[0] + ".jpg")  # Cambia la extensión según tus imágenes

            if not os.path.exists(imagen_path):
                print(f"Eliminando {txt_path} (sin imagen correspondiente)")
                os.remove(txt_path)

# Ejemplo de uso para eliminar archivos .txt sin imágenes correspondientes
# Ejemplo de uso para eliminar imágenes sin archivos de texto
imagenes_folder = 'C:/Users/Josemari/Desktop/Images_RGB'
eliminar_txt_sin_imagenes(imagenes_folder)



