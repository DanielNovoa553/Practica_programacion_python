import os

def rename_photos(folder_path):
    # Obtener la lista de archivos en la carpeta
    file_list = os.listdir(folder_path)
    index = 0
    # Iterar sobre cada archivo
    for index, file_name in enumerate(file_list):
        # Obtener la extensión del archivo
        file_extension = os.path.splitext(file_name)[1]

        # Crear un nuevo nombre de archivo utilizando un formato deseado
        new_file_name = f"Xcaret_Vacaciones_06_2023_{index + 1}{file_extension}"

        # Construir la ruta completa tanto para el archivo antiguo como para el nuevo
        old_file_path = os.path.join(folder_path, file_name)
        new_file_path = os.path.join(folder_path, new_file_name)

        # Renombrar el archivo
        os.rename(old_file_path, new_file_path)

        # Imprimir el cambio realizado
        print(f"Renombrado: {file_name} -> {new_file_name}")

# Ruta de la carpeta que contiene las fotos
folder_path = "C:/Users/danie/OneDrive/Escritorio/Xcaret2023"

# Llamar a la función para renombrar las fotos
rename_photos(folder_path)
