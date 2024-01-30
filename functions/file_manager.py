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
    




    

