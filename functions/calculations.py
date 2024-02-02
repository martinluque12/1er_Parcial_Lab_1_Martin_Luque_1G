from validations import *

def calculate_subtotal_purchase(product: dict) -> float:
    """Calcula el subtotal de una compra (Cantidad x valor del producto)

    Args:
        product (dict): El diccionario que representa un producto.

    Returns:
        float: El subtotal del producto.
    """
    if validate_dict(product):

        subtotal_purchase = product["precio"] * product["cantidad"]

        return subtotal_purchase


def calculate_total_purchase(product_list: list) -> float:
    """Calcula el total de una compra. 

    Args:
        product_list (list): La lista de diccionarios que tiene la info de los productos que se van a comprar.

    Returns:
        float: El total de la compra.
    """
    if validate_list(product_list):

        total_purchase = 0

        for product in product_list:
            total_purchase += product["precio"] * product["cantidad"]
    
        return total_purchase