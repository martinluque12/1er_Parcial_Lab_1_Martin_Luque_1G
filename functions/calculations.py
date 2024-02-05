from functools import reduce
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

        total_purchase = reduce(lambda acc, product: acc + (product["precio"] * product["cantidad"]), product_list, 0)
        return round(total_purchase, 2)
    

def apply_increase(increase: float, value: float) -> float:
    """Aplica un aumento a una variable de tipo float.

    Args:
        increase (float): El aumento que se aplicara.
        value (float): La variable sobre la cual se va a aplicar el aumento.

    Returns:
        float: EL resultado de aplicarle el aumento a la variable.
    """
    if isinstance(increase, float) and isinstance(value, float):

        result = value + (increase * value) // 100

        return round(result, 2)
    
    else:
        return 0


def apply_price_increase_product(product: dict) -> dict:
    """Aplica un aumento al precio de un producto.

    Args:
        product (dict): El producto al cual se le aplicara el aumento.

    Returns:
        dict: El producto con el precio actualizado.
    """
    if validate_dict(product):
        increase = 8.4
        product["precio"] = apply_increase(increase, product["precio"])

        return product
    else:
        return {}
    


