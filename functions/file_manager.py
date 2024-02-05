import os
import json
import csv
from validations import *
from casteos import *
from string_manipulation import *


def read_csv_file(file_path: str) -> list:
    """Lee el archivo CSV y lo guarda en una lista de diccionarios.

    Args:
        file_path (str): La ruta del archivo CSV.

    Returns:
        list: La lista de diccionarios con la información de los insumos.
    """
    if validate_str(file_path):

        with open (file_path, 'r', encoding='utf-8') as csv_file:

            lines = csv_file.readlines()
            
        return lines

    else:
        return []
    

def generate_txt_file(content: str, folder_path: str, file_name: str) -> bool:
    """Genera un archivo TXT.

    Args:
        content (str): El contenido que tendrá el archivo.
        folder_path (str): La ruta del archivo.
        file_name (str): El nombre que tendrá el archivo.

    Returns:
        bool: True si se pudo crear el archivo TXT, False de lo contrario.
    """
    if validate_str(content) and validate_str(folder_path) and validate_str(file_name):

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        full_path = os.path.join(folder_path, file_name)

        with open(full_path, "w") as txt_file:
            txt_file.write(content)
            return True
    
    else:
        return False


def get_last_invoice_number() -> int:
    """Obtiene el ultimo número de factura emitida.

    Returns:
        int: El numero de la ultima factura emitida.
    """
    try:
        with open("last_invoice_number.txt", "r") as file:
            return int(file.read().strip())
        
    except FileNotFoundError:
        return 0  


def update_last_invoice_number(new_number: int) -> None:
    """Actualiza el numero de la factura que se emitirá.

    Args:
        new_number (int): El numero de la nueva factura a emitir.
    """
    with open("last_invoice_number.txt", "w") as file:
        file.write(str(new_number))


def save_list_json_file(data_list: list, folder_path: str, file_name: str) -> bool:
    """Guarda una lista en un archivo JSON.

    Args:
        data_list (list): La lista a guardar.
        folder_path (str): La ruta del archivo.
        file_name (str): El nombre que tendrá el archivo.

    Returns:
        bool: True si se pude generar el archivo JSON, False de lo contrario.
    """
    if validate_list(data_list) and validate_str(folder_path) and validate_str(file_name):

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        full_path = os.path.join(folder_path, file_name)

        with open (full_path, 'w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file, indent=2, ensure_ascii=False)
            return True
    
    else:
        return False
    

def save_list_hard_drive_json_file(product_list: list) -> None:
    """Guarda la lista filtrada de productos que en su nombre tengan las palabras "Disco duro" en un archivo JSON.

    Args:
        product_list (list): La lista de productos que se guardara en el archivo JSON.
    """
    if validate_list(product_list):
        folder_path = "1er_Parcial_Lab_1_Martin_Luque_1G\\json_file"
        file_name  = "Lista_Productos_Disco_Duro.json"
        if save_list_json_file(product_list, folder_path, file_name):
            print("\nLista guardada en archivo JSON exitosamente.")
        else:
            print("\nError al guardar lista en archivo JSON.")
    else:
        print("\n¡Error! Origen de datos no valido.")


def read_json_file(folder_path: str, file_name: str) -> list:
    """Lee un archivo json y lo convierte en una lista de diccionarios.

    Args:
        folder_path (str): La ruta del archivo.
        file_name (str): El nombre del archivo.

    Returns:
        list: Una lista de diccionarios con el contenido leído.
    """
    if validate_str(folder_path) and validate_str(file_name):

        full_path = os.path.join(folder_path, file_name)

        if os.path.exists(full_path):
            with open(full_path, 'r', encoding='utf-8') as json_file:

                data_list = json.load(json_file)
                return data_list
            0
        else:
            return []
    else:
        return []
    

def save_list_csv_file(data_list: list, folder_path: str, file_name: str) -> bool:
    """Guarda una lista de diccionarios en un archivo CSV.

    Args:
        data_list (list): La lista que se guardará en el archivo CSV.
        folder_path (str): La ruta de la carpeta del archivo CSV.
        file_name (str): El nombre del archivo CSV.

    Returns:
        bool: True si se pudo guardar el archivo CSV, False de lo contrario.
    """
    if validate_list(data_list) and validate_str(folder_path) and validate_str(file_name):
        full_path = os.path.join(folder_path, file_name)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        with open(full_path, 'w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=data_list[0].keys())
            csv_writer.writeheader()
            csv_writer.writerows(data_list)

        return True
    else:
        return False
