import os
import shutil
from sklearn.model_selection import train_test_split

def split_dataset(input_folder, output_folder, train_size=0.7, val_size=0.15, test_size=0.15, random_seed=42):
    # Obtener la lista de archivos de imágenes y anotaciones
    image_files = os.listdir(os.path.join(input_folder, 'images'))
    annotation_files = os.listdir(os.path.join(input_folder, 'annotations'))

    # Dividir los datos en conjuntos de entrenamiento, validación y prueba
    train_images, test_images = train_test_split(image_files, test_size=val_size + test_size, random_state=random_seed)
    val_images, test_images = train_test_split(test_images, test_size=test_size / (val_size + test_size), random_state=random_seed)

    # Crear carpetas de salida
    os.makedirs(os.path.join(output_folder, 'images', 'train'), exist_ok=True)
    os.makedirs(os.path.join(output_folder, 'images', 'validation'), exist_ok=True)
    os.makedirs(os.path.join(output_folder, 'images', 'test'), exist_ok=True)
    
    os.makedirs(os.path.join(output_folder, 'labels', 'train'), exist_ok=True)
    os.makedirs(os.path.join(output_folder, 'labels', 'validation'), exist_ok=True)
    os.makedirs(os.path.join(output_folder, 'labels', 'test'), exist_ok=True)

    # Copiar archivos a las carpetas correspondientes
    for image_file in train_images:
        # Copiar imágenes
        shutil.copy(os.path.join(input_folder, 'images', image_file), os.path.join(output_folder, 'images', 'train'))
        # Copiar anotaciones
        shutil.copy(os.path.join(input_folder, 'annotations', image_file.replace(os.path.splitext(image_file)[1], '.txt')), os.path.join(output_folder, 'labels', 'train'))

    for image_file in val_images:
        # Copiar imágenes
        shutil.copy(os.path.join(input_folder, 'images', image_file), os.path.join(output_folder, 'images', 'validation'))
        # Copiar anotaciones
        shutil.copy(os.path.join(input_folder, 'annotations', image_file.replace(os.path.splitext(image_file)[1], '.txt')), os.path.join(output_folder, 'labels', 'validation'))

    for image_file in test_images:
        # Copiar imágenes
        shutil.copy(os.path.join(input_folder, 'images', image_file), os.path.join(output_folder, 'images', 'test'))
        # Copiar anotaciones
        shutil.copy(os.path.join(input_folder, 'annotations', image_file.replace(os.path.splitext(image_file)[1], '.txt')), os.path.join(output_folder, 'labels', 'test'))


if __name__ == "__main__":
    input_folder = "C:/Users/Josemari/Desktop/Images_RGB/DatasetCrudo"
    output_folder = "C:/Users/Josemari/Desktop/PruebasIA/datasets"

    split_dataset(input_folder, output_folder)
