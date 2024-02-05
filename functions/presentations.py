from file_manager import *
from console_functions import *
from data_manipulation import *
from user_input import *
from calculations import *
from purchase import *


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


def infobaus_search_product_by_feature(data_list: list) -> None:
    """Busca y muestra los productos por características. 

    Args:
        data_list (list): La lista de diccionarios con la info de los insumos.
    """
    if validate_list(data_list):
        
        print_search_product_by_feature(data_list)
    
    else:
        print("\n¡Error! Origen de datos no validos.")


def infobaus_sort_list_by_price_and_brand(data_list: list) -> None:
    """Ordena una lista de diccionarios según el precio en descendente y luego por marca en ascendente.

    Args:
        data_list (list): La lista de diccionarios con la info de los insumos.
    """
    if validate_list(data_list):

        sorted_list = sort_list_by_two_keys(data_list, "precio", "marca")
        print_list_supplies_sorted(sorted_list)

    else:
        print("\n¡Error! Origen de datos no valido.")

    
def infobaus_make_purchase(product_list: list) -> None:
    """Realiza las compras de productos.

    Args:
        product_list (list): La lista de diccionarios con la info de los insumos.
    """
    if validate_list(product_list):
        list_purchase = make_purchase(product_list)
        print_purchase_total(list_purchase)


def infobaus_save_list_hard_drive_json_file(product_list: list) -> None:
    """Guarda la lista de diccionarios filtrada por productos que en su nombre tengan las palabras "Disco duro",
       en un archivo JSON.

    Args:
        product_list (list): La lista de diccionarios con la info de los insumos.
    """
    if validate_list(product_list):

        hard_drive_products = filter_list_hard_drive_product(product_list)
        save_list_hard_drive_json_file(hard_drive_products)
    else:
        print("\n¡Error! Origen de datos no valido")


def infobaus_read_json_file_hard_drive_products() -> None: 
    """Lee el archivo JSON de los productos disco duro y los muestra por consola.
    """
    folder_path = "1er_Parcial_Lab_1_Martin_Luque_1G\\json_file\\"
    file_name = "Lista_Productos_Disco_Duro.json"
    products_hard_drive = read_json_file(folder_path, file_name)
    print_list_hard_drive_products(products_hard_drive)


def infobaus_update_csv_file_supplies(product_list: list) -> None:
    """Actualiza el archivo CSV con la info de los productos actualizadas.

    Args:
        product_list (list): La lista de diccionarios con la info de los insumos.
    """
    if validate_list(product_list):

        update_list = update_product_prices(product_list)
        folder_path = "1er_Parcial_Lab_1_Martin_Luque_1G\\csv_file\productos_actualizados.csv"
        if save_list_csv_file(update_list, folder_path):
            print("\nArchivo CSV actualizado correctamente.")
        else:
            print("\nError al intentar actualizar el archivo CSV.")
    else:
        print("\n¡Error! Origen de datos no valido.")


lista = infobaus_read_csv_file_supplies()



