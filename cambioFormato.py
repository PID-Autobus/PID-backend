import os
import yaml

def convert_folder_to_yolo(input_folder, output_folder):
    yolo_labels = {
        'pedestrian': 0,
        'wheelchair': 1,
        'push-wheelchair': 2,
        'crutches': 3,
        'walking_frame': 4
    }

    # Verificar si la carpeta de salida existe, si no, crearla
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterar sobre los archivos YAML en la carpeta de entrada
    for filename in os.listdir(input_folder):
        if filename.endswith(".yml") or filename.endswith(".yaml"):
            yaml_file_path = os.path.join(input_folder, filename)
            output_txt_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".txt")
            convert_yaml_to_yolo(yaml_file_path, output_txt_path, yolo_labels)

def convert_yaml_to_yolo(yaml_file_path, output_txt_path, yolo_labels):
    with open(yaml_file_path, 'r') as yaml_file:
        data = yaml.load(yaml_file, Loader=yaml.FullLoader)

    with open(output_txt_path, 'w') as output_txt:
        if 'object' not in data['annotation']:
            return  # No hay objetos en este archivo YAML, pasar al siguiente

        for obj in data['annotation']['object']:
            label = obj['name']
            if label in yolo_labels:
                label_id = yolo_labels[label]
                bbox = obj['bndbox']
                xmin = int(float(bbox['xmin']))
                ymin = int(float(bbox['ymin']))
                xmax = int(float(bbox['xmax']))
                ymax = int(float(bbox['ymax']))

                width = int(data['annotation']['size']['width'])
                height = int(data['annotation']['size']['height'])

                x_center = (xmin + xmax) / (2 * width)
                y_center = (ymin + ymax) / (2 * height)
                box_width = (xmax - xmin) / width
                box_height = (ymax - ymin) / height

                output_txt.write(f"{label_id} {x_center:.6f} {y_center:.6f} {box_width:.6f} {box_height:.6f}\n")

# Ejemplo de uso para convertir una carpeta de archivos YAML
input_folder = 'C:/Users/Josemari/Desktop/Images_RGB/Annotations_RGB'
output_folder = 'C:/Users/Josemari/Desktop/Images_RGB'
convert_folder_to_yolo(input_folder, output_folder)
