from validations import *
from searches import *
from casteos import *


def request_data_user(message: str) -> str:
    """Le pide al usuario que ingrese un dato.

    Args:
        message (str): El mensaje que se le mostrara al usuario.

    Returns:
        str: Lo que haya ingresado el usuario.
    """
    if validate_str(message):

        user_input = input(message + " > ").lower()

        return user_input
    
    else:
        return ""
    

def request_brand_user(product_list: list) -> str:
    """Le pide al usuario que ingrese una marca, valida que la marca exista en la lista de diccionarios.

    Args:
        product_list (list): La lista de diccionarios con la info de los insumos.

    Returns:
        str: La marca ingresada por el usuario.
    """
    if validate_list(product_list):    

        flag_brand = False
        while True:

            brand = request_data_user("\nIngrese la marca")

            for product in product_list:
                if search_match(brand, product["marca"]):
                    flag_brand = True
                    return brand
            
            if not flag_brand:
                print("\n¡Error! Marca no encontrada, vuelva a intentarlo.\n")
                continue
    else:
        return ""
    

def request_id_user(product_list: list) -> dict:
    """Le pide al usuario que ingrese el ID del producto que quiere comprar.

    Args:
        product_list (list): La lista de diccionarios filtrada por marca.

    Returns:
        dict: El diccionarios que representa el producto con el ID que el usuario ingreso.
    """
    if validate_list(product_list):

        flag_id = False
        while True:

            product_id = request_data_user("\nIngrese el ID del producto que quiere agregar al carrito")
            if validate_int(product_id):
                product_id = castear_int(product_id)
            else:
                print("\n¡Error! Debe ingresar caracteres numéricos, vuelva a intentarlo.\n")
                continue

            for product in product_list:
                if product['id'] == product_id:
                    flag_id = True
                    return product
                
            if not flag_id:
                print("\n¡Error! El ID ingresado no corresponde a ninguno de los producto, vuelva a intentarlo.")
                continue
    else:
        return {}
    

def request_quantity_user() -> int:
    """Le pide al usuario que ingrese la cantidad que quiere comprar.

    Returns:
        int: La cantidad casteada a int.
    """
    while True:

        quantity = request_data_user("\nIngrese la cantidad que quiere comprar")
        if validate_int(quantity):
            return castear_int(quantity)
        else:
            print("\n¡Error! Debe ingresar solo caracteres numéricos, vuelva a intentarlo.\n")
            continue
    

def request_confirmation_user(message: str) -> bool:
    """Le pide al usuario una confirmación.

    Args:
        message (str): El mensaje que se le mostrara al usuario.

    Returns:
        bool: True si el usuario ingresa "si", False si el usuario ingresa "no", 
              le vuelve a pedir la confirmación si ingresa cualquier otra cosa.
    """
    if validate_str(message):

        while True:
            confirmation = input(f'{message} Responda con "Si" o con "No" > ').lower()

            if confirmation == "si":
                return True
            elif confirmation == "no":
                return False
            else:
                print('\n¡Error! Solo puede responder con "Si" o con "No", vuelva a intentarlo.')
                continue
    else:
        return False
    

def request_option_user(menu: str) -> str | int:
    """Le pide al usuario que ingrese una opción para desplazarse por el menu de opciones.

    Returns:
        str | int: Devuelve un string que representa la opción elegida por el usuario o -1 en caso de error.
    """
    print(menu)

    option = input("   > ")
    if re.search("^\d+$", option) and 0 <= int(option) <= 11:
        return option
    else:
        return -1