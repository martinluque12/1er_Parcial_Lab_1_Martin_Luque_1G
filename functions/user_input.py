from validations import *


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