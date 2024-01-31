from validations import *
from file_manager import *
from string_manipulation import *
from searches import *

def return_supplies_list() -> list:
    """Retorna la lista de insumos con algunas mejoras.

    Returns:
        list: La lista de diccionarios mejorada.
    """
    
    data_list = read_csv_file("1er_Parcial_Lab_1_Martin_Luque_1G\\csv_file\\Insumos.csv - Hoja 1.csv")

    supplies = []

    header = data_list[0].split(',')
    header = [key.replace('"', '').strip().lower() for key in header]

    for line in data_list[1:]:
        line = line.split(',')
        line = [value.replace('"', '').replace('$', '').strip() for value in line]
        line = [value.replace('|!*|', ', ') for value in line]

        products = {
            header[0]: castear_int(line[0]),
            header[1]: capitalize_word(line[1]),
            header[2]: capitalize_word(line[2]),
            header[3]: castear_float(line[3]),
            header[4]: line[4]
        }

        supplies.append(products)

    return supplies
    

def filter_list_by_key_and_item(data_list: list, key: str) -> dict:
    """Filtra una lista de diccionarios por una clave y guarda los items que tiene cada clave en una lista.

    Args:
        data_list (list): La lista de diccionarios que se va a filtrar.
        key (str): La clave por la que se va a filtrar.

    Returns:
        dict: Un diccionario que como clave tendrá el valor de la calve y como valor tendrá una lista
              con los items que tiene cada clave.
    """
    if validate_list(data_list) and validate_str(key) and validate_key_in_list_dict(data_list, key):

        data = {}

        for item in data_list:
            if item[key] not in data:
                data[item[key]] = []
                
            data[item[key]].append(item)

        return data

    return {}


def filter_product_by_key(data_list: list, key: str, value: str) -> list:
    """Filtra una lista de diccionarios según un valor específico en una clave.

    Args:
        data_list (list): La lista de diccionarios a filtrar.
        key (str): La clave por la que se va a filtrar.
        value (str): El valor que se debe encontrar en la clave.

    Returns:
        list: La lista de diccionarios filtrada.
    """
    if(validate_list(data_list) and validate_key_in_list_dict(data_list, key) and
       validate_str(key) and validate_str(value)):

        data = []

        for item in data_list:
            if search_match(value, item["caracteristicas"]):
                data.append(item)

        return data

    else:
        return []