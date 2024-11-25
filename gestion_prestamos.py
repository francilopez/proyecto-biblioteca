import json
import os

def cargar_prestamos(filename):
    # pre: el parámetro filename representa la ruta a un archivo JSON que contiene los datos de los préstamos. 
    # pos: la función carga y retorna el contenido del archivo en forma de un objeto Python 
    """Carga los préstamos desde un archivo JSON."""
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []







def guardar_prestamos(prestamos, filename):
    # pre:  parámetro prestamos sea un objeto Python que contiene la información de los préstamos a guardar. filename representa la ruta y nombre del archivo en el que se guardarán los datos de los préstamos.
    # pos: guarda el objeto prestamos en el archivo especificado por filename en formato JSON
    """Guarda los préstamos en un archivo JSON."""
    with open(filename, 'w') as file:
        json.dump(prestamos, file, indent=4)







def agregar_prestamo(prestamos, filename, id_prestamo, id_libro, id_cliente, fecha_prestamo):
    # pre: parámetro prestamos es una lista de diccionarios, donde cada diccionario representa un préstamo y debe contener las claves 'id', 'id_libro', 'id_cliente', 'fecha_prestamo', y 'estado'.
    # pos: id_prestamo no existe en la lista de préstamos, la función agrega un nuevo préstamo con los datos proporcionados (ID del préstamo, ID del libro, ID del cliente y fecha de préstamo) a la lista prestamos y guarda la lista actualizada en el archivo especificado por filename.
    ids_prestamos = {prestamo['id'] for prestamo in prestamos}  # Conjunto de IDs existentes
    if id_prestamo in ids_prestamos:
        print(f"El préstamo con ID {id_prestamo} ya existe.")
        return
    
    nuevo_prestamo = {
        'id': id_prestamo,
        'id_libro': id_libro,
        'id_cliente': id_cliente,
        'fecha_prestamo': fecha_prestamo,
        'estado': 'prestado'
    }
    prestamos.append(nuevo_prestamo)
    guardar_prestamos(prestamos, filename)  
    print(f"Préstamo agregado: ID={id_prestamo}, Libro ID={id_libro}, Cliente ID={id_cliente}, Fecha={fecha_prestamo}")






# def listar_prestamos(prestamos):
#     """Lista todos los préstamos actuales."""
#     if not prestamos:
#         print("No hay préstamos actuales.")
#     else:
#         print("Historial de Préstamos:")
#         for prestamo in prestamos:
#             print(f"ID: {prestamo['id']}, Libro ID: {prestamo['id_libro']}, Cliente ID: {prestamo['id_cliente']}, Fecha de Préstamo: {prestamo['fecha_prestamo']}, Estado: {prestamo['estado']}")





def listar_prestamos(prestamos):
    # pre: parámetro prestamos es una lista de diccionarios, donde cada diccionario representa un préstamo con las claves 'id', 'id_libro', 'id_cliente', 'fecha_prestamo', y 'estado'.
    # pos: imprime en formato tabular los detalles de cada préstamo en la lista prestamos, mostrando el ID del préstamo, el ID del libro, el ID del cliente, la fecha del préstamo y el estado del préstamo. 
    print(f"{'ID':<5} {'ID Libro':<10} {'ID Cliente':<12} {'Fecha de Préstamo':<20} {'Estado':<10}")
    print("-" * 60)

    for prestamo in prestamos:
     print(f"{prestamo['id']:<5} {prestamo['id_libro']:<10} {prestamo['id_cliente']:<12} {prestamo['fecha_prestamo']:<20} {prestamo['estado']:<10}")
    print("-" * 60)







def actualizar_prestamo(prestamos, filename, id_prestamo, nueva_fecha=None, nuevo_estado=None):
    # pre: parámetro prestamos es una lista de diccionarios, donde cada diccionario representa un préstamo con las claves 'id', 'id_libro', 'id_cliente', 'fecha_prestamo', y 'estado'. El parámetro filename representa la ruta al archivo JSON donde se almacenan los préstamos.
    # pos: se encuentra un préstamo con el id_prestamo especificado, la función actualiza la fecha y/o el estado del préstamo con los valores proporcionados y guarda la lista de préstamos actualizada en el archivo especificado por filename
    for prestamo in prestamos:
        if prestamo['id'] == id_prestamo:
            if nueva_fecha:
                prestamo['fecha_prestamo'] = nueva_fecha
            if nuevo_estado:
                prestamo['estado'] = nuevo_estado
            guardar_prestamos(prestamos, filename)  # Guardar cambios
            print(f"Préstamo con ID={id_prestamo} actualizado: Fecha={prestamo['fecha_prestamo']}, Estado={prestamo['estado']}")
            return
    print(f"No se encontró el préstamo con ID={id_prestamo}")







def registrar_devolucion(prestamos, filename, id_prestamo):
    # pre:  parámetro prestamos es una lista de diccionarios, donde cada diccionario representa un préstamo con las claves 'id', 'id_libro', 'id_cliente', 'fecha_prestamo', y 'estado'. El parámetro filename representa la ruta al archivo JSON donde se almacenan los préstamos.
    # pos: actualizar el estado del préstamo especificado por id_prestamo y cambiarlo a 'devuelto'. Después de la actualización, guarda los cambios en el archivo especificado por filename.
    actualizar_prestamo(prestamos, filename, id_prestamo, nuevo_estado='devuelto')




