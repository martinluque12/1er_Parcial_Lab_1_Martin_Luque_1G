from validations import *
from data_manipulation import *
from console_functions import *
from calculations import *
from file_manager import *


def load_shopping_cart(product_list: list) -> list:
    """Carga el carrito de compras con el producto seleccionado por el usuario.

    Args:
        product_list (list): La lista de diccionarios con la info de los insumos.

    Returns:
        list: La lista de diccionarios con los productos seleccionados por el usuario.
    """
    if validate_list(product_list):
        shopping_cart = []

        product_list_brand = filter_list_by_brand(product_list)
        if product_list_brand:
            print_list_supplies(product_list_brand)

        selected_product = request_id_user(product_list_brand)
        quantity = request_quantity_user()
        product = add_key_int_dict(selected_product ,  "cantidad", quantity )

        shopping_cart.append(product)
        return shopping_cart


def make_purchase(product_list: list) -> list:
    """Realiza las compras de los productos que ingreso el usuario.

    Args:
        product_list (list): La lista de diccionarios con la info de los insumos.

    Returns:
        list: Una lista de diccionarios con los productos seleccionados por el usuario.
    """
    if validate_list(product_list):
        shopping_cart = []

        while True:
            purchase = load_shopping_cart(product_list)
            shopping_cart.extend(purchase)

            continue_shopping = request_confirmation_user("\n¿Quiere seguir comprando?")
            if continue_shopping:
                continue
            else:
                return shopping_cart
            
    else:
        return []





def generate_invoice_purchase(product_list: list) -> bool:
    """Genera la factura de la compra.

    Args:
        product_list (list): La lista de diccionarios con los productos comprados.

    Returns:
        bool: True si genero la factura, False de lo contrario.
    """
    if validate_list(product_list):
        content_invoice = generate_purchase_summary(product_list)
        folder_path = "1er_Parcial_Lab_1_Martin_Luque_1G\\invoices"
        invoice_number = get_last_invoice_number()
        file_name = f"Factura_{invoice_number}.txt"

        if generate_txt_file(content_invoice, folder_path, file_name):
            update_last_invoice_number(invoice_number + 1)
            return True
        else:
            return False
        
    
def generate_purchase_summary(product_list: list) -> str:
    """Genera un resumen de la compra en formato texto.

    Args:
        product_list (list): La lista de diccionarios con los productos que se compraran.

    Returns:
        str: El resumen de la compra en formato texto.
    """
    if validate_list(product_list):

        print()
        text = generate_separator("=", 140, False)
        text += "\nTotal de la compra:\n"
        text += generate_separator("=", 140, False)
        text += "\nCantidad".ljust(14) + "Producto".ljust(51) + "Marca".ljust(19) + "Precio U".ljust(12) + "Subtotal"

        for product in product_list:
            subtotal = calculate_subtotal_purchase(product)
            quantity = product['cantidad']
            brand = product['marca']
            name = product["nombre"].replace(brand + ' ', '')
            price = product['precio']
            text += f"\n   {quantity:<9} {name:<50} {brand:<18} ${price:<10} ${subtotal:.2f}\n"
            
        total_purchase = calculate_total_purchase(product_list)

        text += generate_separator("=", 140, False)
        text += "\n".ljust(84) + f"Total: {total_purchase}"

        return text
    

def print_purchase_total(product_list: list) -> None:
    """Muestra el monto total de la compra por pantalla. Pide que se confirme la compra

    Args:
        product_list (list): La lista de diccionarios con los productos que se compraran.
    """
    if validate_list(product_list):
        text_total_purchase = generate_purchase_summary(product_list)

        print(text_total_purchase)

        confirm_purchase = request_confirmation_user("\n¿Confirma la compra?")
        if confirm_purchase and generate_invoice_purchase(product_list):
            print("\nCompra confirmada.")
            print("\nFactura generada exitosamente")
        else:
            print("\nCompra cancelada.")