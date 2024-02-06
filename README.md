<div align="center">
   <h1>🖥️Administrador de Insumos para InfoBaus🖥️</h1>
</div>
<div>
  <h2>📱Este es un programa diseñado para administrar los insumos de InfoBaus, permitiendo al usuario realizar diversas operaciones como la gestión de datos desde un archivo CSV, listar insumos por marca, buscar insumos por características, realizar compras, entre otras funciones.📱</h2>
</div>

<h2>Funcionalidades</h2>

* Traer datos desde archivo: Carga el contenido del archivo Insumos.csv en una colección, teniendo en cuenta las características de los insumos.

* Listar cantidad por marca: Muestra todas las marcas disponibles junto con la cantidad de insumos que corresponden a cada una.

* Listar insumos por marca: Muestra cada marca con el nombre del insumo y su precio correspondiente.

* Buscar insumo por característica: Permite buscar insumos que posean una característica específica ingresada por el usuario.

* Listar insumos ordenados: Muestra los insumos ordenados por marca y, ante marcas iguales, por precio descendente, mostrando el ID, descripción, precio, marca y la primera característica de cada producto.

* Realizar compras: Permite al usuario seleccionar productos de una marca y agregarlos al carrito de compras. Al finalizar, muestra el total de la compra y genera un archivo TXT con la factura si el usuario acepta la compra.

* Guardar Json: Genera un archivo JSON con todos los productos cuyo nombre contenga "Disco Duro".

* Leer Json: Muestra un listado con los insumos guardados en el archivo JSON generado en la opción 7.

* Actualizar precios: Aplica un aumento del 8.4% a todos los productos debido a la inflación y guarda los productos actualizados en el archivo Insumos.csv.

* Agregar nuevo producto: Permite agregar un nuevo producto a la lista.

* Guardar datos actualizados: Permite al usuario elegir el formato de exportación (CSV o JSON) y guarda todos los datos actualizados, incluyendo las altas.

<h2>Requerimientos: </h2>

* Python 3.x

* Archivos Insumos.csv, marcas.txt
  
* Librerías: json
  
<h2>Uso</h2>

* Clona el repositorio o descarga los archivos.

* Ejecuta el programa main.py.
  
* Sigue las instrucciones en pantalla para utilizar las diferentes funcionalidades del programa.

<div align="center">
  <h1>🕹️¡Disfruta administrando tus insumos con InfoBaus!🕹️</h1>
