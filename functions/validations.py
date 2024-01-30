import re

def validate_str(string: str) -> bool:
    """Valida que una variable sea de tipo str y que no este vacía.

    Args:
        string (str): La variable a validar.

    Returns:
        bool: True si la variable es de tipo str, False de lo contrario.
    """
    if isinstance(string, str) and string:
        return True
    else:
        return False
    

def validate_int(number: str) -> bool:
    """Valida mediante RegEx que una variable de tipo str contenga solo caracteres numéricos enteros.

    Args:
        number (str): La variable a validar.

    Returns:
        bool: True si contiene solo caracteres numéricos enteros, False de lo contrario.
    """
    if validate_str(number):

        pattern = re.compile(r'^[+-]?\d+$')

        if pattern.match(number):
            return True
        else:
            return False
    else:
        return False
    

def validate_float(number: str) -> bool:
    """Valida mediante RegEx que una variable de tipo str solo contenga caracteres de punto flotante. 

    Args:
        number (str): La variable a validar.

    Returns:
        bool: True si contiene solo caracteres de punto flotante, False de lo contrario.
    """
    if validate_str(number):

        pattern = re.compile(r'^[+-]?\d+(\.\d+)+$')
        
        if pattern.match(number):
            return True
        else:
            return False
    else:
        return False
    

def validate_list(data_list: list) -> bool:
    """Valida que una variable sea de tipo list y que la lista no esta vacía.

    Args:
        data_list (list): La variable a validar.

    Returns:
        bool: True si es de tipo list y no esta vacía, False de lo contrario.
    """
    if isinstance(data_list, list) and data_list:
        return True
    else:
        return  False


def validate_dict(dictionary: dict) -> bool:
    """Valida que una variable sea de tipo dict y que no este vacío

    Args:
        dictionary (dict): La variable a validar.

    Returns:
        bool: True si es de tipo dict y no esta vacío, False de lo contrario.
    """
    if isinstance(dictionary, dict) and dictionary:
        return True
    else:
        return False


def validate_key_in_list_dict(list_dict: list, key: str) -> bool:
    """Valida que una clave se encuentre en una lista de diccionarios.

    Args:
        list_dict (list): La lista de diccionarios en donde se buscara la clave.
        key (str): La clave a buscar en el diccionario.

    Returns:
        bool: True si la clave se encuentra en la lista de diccionarios, False de lo contrario.
    """
    if validate_list(list_dict) and validate_str(key):

        for dictionary in list_dict:
            for k in dictionary.keys():
                if k == key:
                    return True
                
        return False
    
    return False


def validate_key_in_dict(dictionary: dict, key: str) -> bool:
    """Valida que una calve se encuentre en un diccionarios.

    Args:
        dictionary (dict): El diccionario donde se buscará la clave.
        key (str): La clave a buscar.

    Returns:
        bool: True si la calve se encuentra en el diccionario, False de lo contrario.
    """
    if validate_dict(dictionary) and validate_str(key):
        for k in dictionary.keys():
            if k == key:
                return True
        
        return False
    
    else: 
        return False
    
