from validations import *
from file_manager import *
from string_manipulation import *
from searches import *
from user_input import *
from calculations import *


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
            if search_match(value, item[key]):
                data.append(item)

        return data

    else:
        return []
    

def sort_list_by_two_keys(data_list: list, key_one: str, key_two:str) -> list:
    """Ordena una lista de diccionarios por dos claves primero de forma descendente y luego de forma ascendente.

    Args:
        data_list (list): La lista de diccionarios a ordenar.
        key_one (str): La primer clave por la que se va a ordenar.
        key_two (str): La segunda clave por la que se va a ordenar.

    Returns:
        list: La lista ordenada.
    """
    if(validate_list(data_list) and validate_key_in_list_dict(data_list, key_one) and
       validate_key_in_list_dict(data_list, key_two) and validate_str(key_one) and validate_str(key_two)):
        
        size_list = len(data_list)

        for i in range(0, size_list -1):
            for j in range(i + 1, size_list):

                if data_list[i][key_one] < data_list[j][key_one]:
                    data_list[i], data_list[j] = data_list[j], data_list[i]
                elif data_list[i][key_one] == data_list[j][key_one]:
                    if data_list[i][key_two] > data_list[j][key_two]:
                        data_list[i], data_list[j] = data_list[j], data_list[i]

        return data_list
    
    else:
        return []
    

def filter_list_by_brand(product_list: list) -> list:
    """Filtra la lista de diccionarios por una marca ingresada por el usuario.

    Args:
        product_list (list): La lista de diccionarios a filtrar.

    Returns:
        list: Una lista de diccionarios con los productos que sean de la marca ingresada.
    """
    if validate_list(product_list):

        brand = request_brand_user(product_list)

        list_brand = filter_product_by_key(product_list, "marca", brand)
        if list_brand:
            return list_brand
        else:
            return []

    else:
        return []
    

def add_key_int_dict(dictionary: dict, key: str, value: int) -> dict:
    """Agrega una nueva clave a un diccionario y le asigna un valor entero.

    Args:
        dictionary (dict): El diccionario al cual se le agregara la nueva clave.
        key (str): La clave que se agregara.
        value (int): El valor que tendrá la clave

    Returns:
        dict: El diccionario con la nueva clave ya agregada.
    """
    if validate_dict(dictionary) and validate_str(key) and isinstance(value, int):

        dictionary[key.lower()] = value
        return dictionary
    else:
        return {}
    

def filter_list_hard_drive_product(product_list: list) -> list:
    """Filtra la lista de diccionarios por los productos que en su nombre lleven las palabras "Disco Duro".

    Args:
        product_list (list): La lista de diccionarios a filtrar.

    Returns:
        list: Una lista de diccionarios con los productos que en su nombre lleven las palabras "Disco Duro".
    """
    if validate_list(product_list):

        hard_drive_products = filter_product_by_key(product_list, "nombre", "Disco Duro")
        return hard_drive_products
    else:
        return []
    

def update_product_prices(product_list: list) -> list:

    if validate_list(product_list):
        update_products = list(map(apply_price_increase_product, product_list))

        return update_products
    else:
        return []