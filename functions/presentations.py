from file_manager import *
from console_functions import *
from data_manipulation import *


def infobaus_read_csv_file_supplies() -> list:
    """Lee el archivo CSV con la info de los insumos mediante la función "read_csv_file_supplies()"
       y lo convierte en una lista de diccionarios.

    Returns:
        list: La lista de diccionarios con la información de los insumos.
    """
    list_supplies = return_supplies_list()

    if list_supplies:

        print("\nSe ha leído el archivo correctamente.")
        return list_supplies
    
    else:
        print("\nError al leer el archivo.")
        return []
    

def infobaus_show_brand_and_quantity(data_list: list) -> None:
    """Filtra  la lista de productos para mostrar solo las marcas y las cantidades de cada una.

    Args:
        data_list (list): La lista de diccionarios con la info de los insumos.
    """
    if validate_list(data_list):

        dictionary = filter_list_by_key_and_item(data_list, "marca")
        print_list_filtered_by_brand_and_quantity(dictionary)
    else:
        print("\nOrigen de datos no valido.")


def infobaus_show_brand_and_products(data_list: list) -> None:
    """Filtra  la lista de productos para mostrar solo las marcas y los productos que tienen cada marca.

    Args:
        data_list (list): La lista de diccionarios con la info de los insumos.
    """
    if validate_list(data_list):

        dictionary = filter_list_by_key_and_item(data_list, "marca")
        print_list_filtered_by_brand_and_products(dictionary)
    else:
        print("\nOrigen de datos no valido.") 


