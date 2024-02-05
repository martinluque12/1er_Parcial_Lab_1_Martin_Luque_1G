import os
import platform
from validations import *
from user_input import *
from data_manipulation import *


def clear_screen() -> None:
    """Limpia la consola.
    """
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def generate_separator(pattern: str, long: int, imprimir: bool = True) -> None | str:
    """Genera un separador, conformado por el patron por el largo.

    Args:
        pattern (str): El carácter a mostrar. 
        long (int): El largo del separador.
        imprimir (bool, optional): Parámetro opcional, verifica si se debe imprimir o no. Defaults to True.

    Returns:
        None | str: Si el parámetro opcional se encentra en True, se imprime por consola el separador generado,
                    si no, solo se retorna el separador generado o si no pasa las validaciones se retornara "".
    """
    if (validate_str(pattern) and (len(pattern) == 1 or len(pattern) == 2) and
        isinstance(long, int) and (long > 0 and long < 141)):

        if imprimir:
            print(pattern * long)
        else:
            return pattern * long
    else:
        return ""
    

def print_list_supplies(data_list: list) -> None:
    """Imprime la lista de insumos formateada.

    Args:
        data_list (list): La lista de diccionarios con la info de los insumos.
    """
    if validate_list(data_list):

        generate_separator("-", 140)
        print("\nID:".ljust(7) + "Producto".ljust(51) + "Marca".ljust(19) + "Precio:".ljust(12) + "Características:")

        for product in data_list:
            product_id = product["id"]
            brand = product["marca"]
            name = product["nombre"].replace(brand + ' ', '')
            price = product["precio"]
            feature = product["caracteristicas"]
            print(f"\n{product_id:<5} {name:<50} {brand:<18} ${price:<10} {feature}")
            print()
            generate_separator("-", 140)
    
    else:
        print("\n¡Error! Origen de datos no valido")


def print_list_filtered_by_brand_and_quantity(dictionary: dict) -> None:
    """Imprime por consola las marcas y las cantidad de productos que hay de esa marca.

    Args:
        dictionary (dict): El diccionarios que contiene las marcas y los productos.
    """
    if validate_dict(dictionary):

        generate_separator("=", 140)
        print("\nMarca:                Cantidad:")

        for brand, product in dictionary.items():
            print(f"{brand:<25} {len(product)}")

        print()
        generate_separator("=", 140)

    else:
        print("\nOrigen de datos no validos.")


def print_list_filtered_by_brand_and_products(dictionary: dict) -> None:
    """Imprime por consola las marcas y los productos que tienen esas marca.

    Args:
        dictionary (dict): El diccionario que contiene las marcas y los productos.
    """
    if validate_dict(dictionary):

        generate_separator("*", 140)
        print("\nMarca:                     Producto:")

        for brand, products in dictionary.items():
            print(f"{brand:<25}  {', '.join([product['nombre'].replace(brand + ' ', '') for product in products])}")

        print()
        generate_separator("=", 140)

    else:
        print("\nOrigen de datos no validos.")


def print_search_product_by_feature(data_list: list) -> None:
    """Le pide al usuario que ingrese una característica y le muestra todos los productos
       que tengan esa característica.

    Args:
        data_list (list): La lista de diccionarios con la info de los insumos.
    """
    if validate_list(data_list):

        while True:
            feature = request_data_user("\nIngrese una característica del producto a buscar")
            products_found = filter_product_by_key(data_list, "caracteristicas", feature)
            if products_found:
                print_list_supplies(products_found)
                break
            else:
                print("\nNo se encontraron productos con esa característica.")
                continue

    else:
        print("\n¡Error! Origen de datos no validos.")


def print_list_supplies_sorted(data_list: list) -> None:
    """Imprime por consola la lista ordenada mostrando ID, NOMBRE, PRECIO, MARCA y la primer CARACTERÍSTICA.

    Args:
        data_list (list): La lista ordenada.
    """
    if validate_list(data_list):

        print("\nLista de insumos ordenada por precio descendente y por marca ascendente:\n")
        generate_separator("*", 140)
        print("ID:".ljust(6) + "Producto".ljust(51) + "Precio".ljust(12) + "Marca:".ljust(19) + "Característica:")
        generate_separator("*", 140)

        for product in data_list:
            product_id = product["id"]
            brand = product["marca"]
            name = product["nombre"].replace(brand + ' ', '')
            price = product["precio"]
            feature = product["caracteristicas"].split(',')
            print(f"\n{product_id:<5} {name:<50} ${price:<10} {brand:<18} {feature[0]}")
            print()
            generate_separator("-", 140)

    else:
        print("\n¡Error! Origen de datos no valido.")


def print_list_hard_drive_products(product_list: list) -> None:
    """Imprime por consola la lista de productos disco duro.

    Args:
        product_list (list): La lista de diccionarios con la info de los productos disco duro.
    """
    if validate_list(product_list):

        generate_separator("*", 140)
        print("\nLista de productos Disco Duro:")
        if product_list:
            print_list_supplies(product_list)
        else:
            print("\n¡Lista de productos vacía!")
    else:
        print("\n¡Error! Origen de datos no validos.")


def menu() -> str:
    """Imprime el menu de la app en consola.
    """
    menu = """                          Bienvenidos a *INFOBAUS*

    1 - Trae datos desde el archivo CSV.
    2 - Listar las marcas disponibles y la cantidad de productos de cada marca.
    3 - Listar las marcas y los productos de cada marca.
    4 - Buscar insumo.
    5 - Listar los productos ordenados por precio descendente y por nombre de la A a la Z.
    6 - Realizar compra.
    7 - Guardar en archivo JSON los productos "Disco duro".
    8 - Leer archivo JSON con los productos "Disco duro".
    9 - Actualizar precios.
    0 - Salir del programa.
    __________________________________________________________________________
    """
    return menu