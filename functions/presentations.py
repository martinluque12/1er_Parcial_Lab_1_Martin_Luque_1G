from file_manager import *
from console_functions import *
from data_manipulation import *

def infobaus_read_csv_file_supplies() -> list:
    """Lee el archivo CSV con la info de los insumos mediante la función "read_csv_file_supplies()"
       y lo convierte en una lista de diccionarios.

    Returns:
        list: La lista de diccionarios con la información de los insumos.
    """
    file_path = "1er_Parcial_Lab_1_Martin_Luque_1G\\csv_file\\Insumos.csv - Hoja 1.csv"
    list_supplies = read_csv_file_supplies(file_path)

    if file_path:
        print("Se ha leido el archivo correctamente.")
        return list_supplies
    else:
        print("Error al leer el archivo.")
        return []
    

def infobaus_show_brand_and_quantity(data_list: list) -> None:
    """Filtra  la lista de productos para mostrar solo las marcas y las cantidades de cada una.

    Args:
        data_list (list): La lista de diccionarios con la info de los insumos.
    """
    if validate_list(data_list):

        dictionary = filter_list_by_key_and_quantity(data_list, "marca")
        print_list_filtered_by_brand_and_quantity(dictionary)
    else:
        print("\nOrigen de datos no valido.")

