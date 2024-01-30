from validations import *

def filter_list_by_key_and_quantity(data_list: list, key: str) -> dict:
    """Filtra una lista de diccionarios por una clave y guarda las cantidades de esa clave.

    Args:
        data_list (list): La lista de diccionarios que se va a filtrar.
        key (str): La clave por la que se va a filtrar.

    Returns:
        dict: Un diccionario que como clave tendrá el valor de la calve y como valor tendrán
              las cantidades correspondientes.
    """
    if validate_list(data_list) and validate_str(key) and validate_key_in_list_dict(data_list, key):

        data = {}

        for item in data_list:
            data[item[key]] = 0

        for item in data_list:
            data[item[key]] += 1

        return data
    
    return {}
