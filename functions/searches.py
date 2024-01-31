from validations import *


def search_match(search_pattern: str,  search_in: str) -> bool:
    """Busca si hay coincidencia entre un patron y una cadena.

    Args:
        search_pattern (str): El patron a buscar.
        search_in (str): La cadena en donde buscar.

    Returns:
        bool: True si hay coincidencia entre el patron a buscar y la cadena donde buscar.
    """
    if validate_str(search_pattern) and validate_str(search_in):

        pattern = re.compile(fr'\b{re.escape(search_pattern)}\b', re.IGNORECASE)

        if pattern.search(search_in.lower()):
            return True
        else:
            return False