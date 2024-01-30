import os
import platform
from validations import *


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
    

def print_list_filtered_by_brand_and_quantity(dictionary: dict) -> None:
    """Imprime por consola las marcas con sus respectivas cantidades.

    Args:
        dictionary (dict): El diccionarios que contiene las marcas y las cantidades.
    """
    if validate_dict(dictionary):

        generate_separator("=", 140)
        print("\nMarca:                Cantidad:")

        for brand, quantity in dictionary.items():
            print(f"{brand:<25} {quantity}")

        print()
        generate_separator("=", 140)

    else:
        print("\nOrigen de datos no validos.")


        