import os
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


