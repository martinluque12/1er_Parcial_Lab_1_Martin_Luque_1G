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

        for product in product_list:
            product.pop("cantidad", None)

        update_list = update_product_prices(product_list)
        folder_path = "1er_Parcial_Lab_1_Martin_Luque_1G\\csv_file"
        file_name = "insumos_actualizados.csv"

        if save_list_csv_file(update_list, folder_path, file_name):
            print("\nArchivo CSV actualizado correctamente.")
        else:
            print("\nError al intentar actualizar el archivo CSV.")
    else:
        print("\n¡Error! Origen de datos no válido.")


def infobaus_menu() -> None:
    """Menu principal del Software, permite que el usuario se maneje por el menu de opciones.
    """
    flag_read_csv = False

    while True:
        clear_screen()

        option = request_option_user(menu())

        match option:

            case "1":
                if not flag_read_csv:
                    product_list = infobaus_read_csv_file_supplies()
                    flag_read_csv = True
                else:
                    print("\nYa se han traído los datos desde el archivo CSV.")
            case "2":
                if flag_read_csv:
                    infobaus_show_brand_and_quantity(product_list)
                else:
                    print("\nPrimero, debe leer los datos desde el archivo CSV.")
            case "3":
                if flag_read_csv:
                    infobaus_show_brand_and_products(product_list)
                else:
                    print("\nPrimero, debe leer los datos desde el archivo CSV.")
            case "4":
                if flag_read_csv:
                    infobaus_search_product_by_feature(product_list)
                else:
                    print("\nPrimero, debe leer los datos desde el archivo CSV.")
            case "5":
                if flag_read_csv:
                    infobaus_sort_list_by_price_and_brand(product_list)
                else:
                    print("\nPrimero, debe leer los datos desde el archivo CSV.")
            case "6":
                if flag_read_csv:
                    infobaus_make_purchase(product_list)
                else:
                    print("\nPrimero, debe leer los datos desde el archivo CSV.")
            case "7":
                if flag_read_csv:
                    infobaus_save_list_hard_drive_json_file(product_list)
                else:
                    print("\nPrimero, debe leer los datos desde el archivo CSV.")
            case "8":
                if flag_read_csv:
                    infobaus_read_json_file_hard_drive_products()
                else:
                    print("\nPrimero, debe leer los datos desde el archivo CSV.")
            case "9":
                if flag_read_csv:
                    infobaus_update_csv_file_supplies(product_list)
                else:
                    print("\nPrimero, debe leer los datos desde el archivo CSV.")
            case "10":
                if flag_read_csv:
                    infobaus_add_new_product(product_list)
                else:
                    print("\nPrimero, debe leer los datos desde el archivo CSV.")
            case "11":
                if flag_read_csv:
                    infobaus_save_list_product_file(product_list)
                else:
                    print("\nPrimero, debe leer los datos desde el archivo CSV.")
            case "0":
                if request_confirmation_user("\n¿Desea salir del programa?"):
                    print("\nGracias por usar nuestro software.")
                    break
                else:
                    continue
            case _:
                print("\nOpción no valida, vuelva a intentarlo.")
                
        
        input("\nPresione Enter para continuar...")


def request_product_name() -> str:
    """Solicita al usuario que ingrese un nombre de producto.
    """
    while True:
        product_name = request_data_user("\nIngrese el nombre del producto")
        if product_name:
            return product_name
        else:
            print("\n¡Error! Debe ingresar el nombre del producto, vuelva a intentarlo.")
            continue



def read_txt_file(file_path: str) -> list:
    """Lee un archivo TXT y devuelve una lista con su contenido.

    Args:
        file_path (str): La ruta del archivo TXT.

    Returns:
        list: Una lista con el contenido del archivo TXT.
    """
    if validate_str(file_path):
        lines = []

        with open(file_path, 'r') as txt_file:
            for line in txt_file:
                lines.append(line.strip())

        return lines
    else:
        return []


def convert_list_brand_dict() -> list:
    """Convierte una lista de marcas en una lista de diccionarios con la clave "marca".

    Returns:
        list: Una lista de diccionarios con la clave "marca" y el valor correspondiente.
    """
    brands = read_txt_file("1er_Parcial_Lab_1_Martin_Luque_1G\\txt_file\\marcas.txt")
    list_brand = []

    for brand in brands:
        list_brand.append({"marca": brand})
    
    return list_brand
    


def print_list_brand(brands: list) -> None:
    """Imprime por consola las marcas de una lista de diccionarios.

    Args:
        brands (list): La lista de diccionarios.
    """
    if validate_list(brands):
        print("\nMarcas disponibles:")
        generate_separator("-", 40)

        for i, brand in enumerate(brands, start=1):
            print(f"{i}. {brand['marca']}")

        generate_separator("-", 40)
    else:
        print("\n¡Error! Origen de datos no validos.")


def request_price_product() -> float | int:
    """Le pide al usuario que ingrese un precio para un producto.

    Returns:
        float | int: El precio ingresado por el usuario casteado a float o a int.
    """
    while True:
        price = request_data_user("\nIngrese el precio del producto")
        
        if validate_float(price):
            return castear_float(price)
        elif validate_int(price):
            return castear_int(price)
        else:
            print("\n¡Error! Debe ingresar caracteres numéricos, vuelva a intentarlo.")
            continue

def request_features_product() -> list:
    """Le pide al usuario que ingrese la/las características del producto (Mínima 1, Máxima 3)

    Returns:
        list: Una lista con las características ingresadas.
    """
    features = []
        
    while True:
        feature = request_data_user("\nIngrese la/las características (mínimo 1, máximo 3)")
        features.append(feature)

        if len(features) < 3:
            confirmation = request_confirmation_user("\n¿Quiere seguir ingresando características?")
            if confirmation:
                continue
            else:
                break
        else:
           break

    return features


def convert_list_str(data_list: list) -> str:
    """Convierte una lista de str a un string separado por ", ".

    Args:
        data_list (list): La lista de str que se va convertir en un string.

    Returns:
        str: El string formado por los elementos de la lista y separados por ", ".
    """
    if validate_list(data_list):
        data_str = ", ".join(data_list)
        return data_str


def get_last_id(product_list: list) -> int:
    """Obtiene el ultimo id generado.

    Args:
        product_list (list): La lista de diccionarios con la info de los insumos.

    Returns:
        int: El ultimo id de la lista de diccionarios.
    """
    if validate_list(product_list):

        for product in product_list:
            last_id = product['id']

        return last_id + 1
    else:
        return 0


def request_data_new_product(product_list: list) -> dict:
    """Le pide al usuario que ingrese los datos de un nuevo producto.

    Args:
        product_list (list): La lista de diccionarios con la info de los insumos.

    Returns:
        dict: Un diccionario que represente un producto.
    """
    if validate_list(product_list):
        
        product_id = get_last_id(product_list)
        product_name = request_product_name()
        brand_list = convert_list_brand_dict()
        print_list_brand(brand_list)
        product_brand = request_brand_user(brand_list)
        product_price = request_price_product()
        product_feature = request_features_product()
        product_feature_str = convert_list_str(product_feature)

        new_product = {
        "id": product_id,
        "nombre" : product_name,
        "marca" : product_brand,
        "precio" : product_price,
        "caracteristicas" : product_feature_str
        }

        return new_product


def add_new_product(product_list: list) -> list:
    """Agrega un nuevo producto a la lista de insumos.

    Args:
        product_list (list): La lista de diccionarios a la que se le agregara un nuevo producto.

    Returns:
        list: La lista con el nuevo producto agregado.
    """
    while True:

        new_product = request_data_new_product(product_list)
        product_list.append(new_product)

        if request_confirmation_user("\n¿Quiere seguir ingresando productos?"):
            continue
        else:
            return product_list

def request_extension() -> str:
    """Le pide al usuario que ingrese una extensión en formato .json o .csv

    Returns:
        str: La extension que ingreso el usuario.
    """
    while True:
        file_extension = request_data_user("\nIngrese el formato del archivo que desea exportar (json o csv)")
        if file_extension != "json" and file_extension != "csv":
            print('\n¡Error! Elija entre las opciones disponibles ("json" o "csv")')
            continue
        else:
            return file_extension

def save_list_file(data_list: list) -> None: 
    """Guarda una lista en un archivo JSON o CSV.

    Args:
        data_list (list): La lista que se guardara en el archivo JSON o CSV.
    """
    if validate_list(data_list):

        file_extension = request_extension()
        if file_extension == "json":
            file_path = "1er_Parcial_Lab_1_Martin_Luque_1G\\json_file"
            file_name = "insumos_actualizados.json"
            save_list_json_file(data_list, file_path, file_name)
            print("\nArchivo JSON creado con éxito.")
        else:
            file_path = "1er_Parcial_Lab_1_Martin_Luque_1G\\csv_file"
            file_name = "insumos_actualizados.csv"
            save_list_csv_file(data_list, file_path, file_name)
            print("\nArchivo CSV creado con éxito.")

def infobaus_add_new_product(product_list: list) :
    """Agrega un nuevo producto a la lista de productos.

    Args:
        product_list (list): La lista de diccionarios con la info de los productos.
    """
    if validate_list(product_list):

        add_new_product(product_list)


def infobaus_save_list_product_file(product_list: list) -> None:
    """Guarda en un archivo JSON o CSV la lista de productos.

    Args:
        product_list (list): La lista de diccionarios a guardar en el archivo JSON o CSV.
    """
    if validate_list(product_list):
        save_list_file(product_list)














