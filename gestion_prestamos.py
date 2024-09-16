import datetime


def agregar_prestamo(prestamos, id_prestamo, id_libro, id_cliente, fecha_prestamo):
    """
Pre: prestamos debe ser una lista de diccionarios con los campos id_prestamo, id_libro, id_cliente y fecha_prestamo.
Pos: Si el ID del préstamo ya existe, se imprime un mensaje de error y no se agrega el nuevo préstamo. Si el ID es único, se agrega un nuevo préstamo a la lista y se imprime un mensaje de éxito.
    """
    # Verifica si el préstamo con el mismo ID ya existe
    for prestamo in prestamos:
        if prestamo['id'] == id_prestamo:
            print(f"El préstamo con ID {id_prestamo} ya existe.")
            return
    nuevo_prestamo = {
        'id': id_prestamo,
        'id_libro': id_libro,
        'id_cliente': id_cliente,
        'fecha_prestamo': fecha_prestamo,
        'estado': 'prestado'  # Estado inicial del préstamo
    }
    prestamos.append(nuevo_prestamo)
    print(f"Préstamo agregado: ID={id_prestamo}, Libro ID={id_libro}, Cliente ID={id_cliente}, Fecha={fecha_prestamo}")

def listar_prestamos(prestamos):
    """
Pre: prestamos es una lista de diccionarios, donde cada diccionario contiene los campos 'id', 'id_libro', 'id_cliente', 'fecha_prestamo', y 'estado'.
Pos: Si la lista prestamos está vacía, se imprime un mensaje indicando que no hay préstamos actuales. Si la lista contiene elementos, se imprime el historial de préstamos con la información de cada préstamo.
    """
    if not prestamos:
        print("No hay préstamos actuales.")
    else:
        print("Historial de Préstamos:")
        for prestamo in prestamos:
            print(f"ID: {prestamo['id']}, Libro ID: {prestamo['id_libro']}, Cliente ID: {prestamo['id_cliente']}, Fecha de Préstamo: {prestamo['fecha_prestamo']}, Estado: {prestamo['estado']}")

def actualizar_prestamo(prestamos, id_prestamo, nueva_fecha=None, nuevo_estado=None):
    """
Pre: prestamos debe ser una lista de diccionarios con los campos 'id', 'fecha_prestamo', y 'estado'; id_prestamo se compara con el 'id' en los diccionarios; nueva_fecha y nuevo_estado representan una fecha y un estado, respectivamente.
Pos: Si el préstamo con el ID se encuentra, se actualizarán los campos especificados y se imprime un mensaje de confirmación. Si el ID no se encuentra, se imprime un mensaje diciendo que el préstamo no fue encontrado y la lista no cambia.
    """
    for prestamo in prestamos:
        if prestamo['id'] == id_prestamo:
            if nueva_fecha:
                prestamo['fecha_prestamo'] = nueva_fecha
            if nuevo_estado:
                prestamo['estado'] = nuevo_estado
            print(f"Préstamo con ID={id_prestamo} actualizado: Fecha={prestamo['fecha_prestamo']}, Estado={prestamo['estado']}")
            return
    print(f"No se encontró el préstamo con ID={id_prestamo}")

def registrar_devolucion(prestamos, id_prestamo):
    """
Pre: prestamos es una lista de diccionarios con los campos 'id', 'fecha_prestamo', y 'estado'; id_prestamo tiene que ser comparable con el campo 'id' en los diccionarios.
Pos: La función actualiza el estado del préstamo con el id_prestamo como 'devuelto'. La lista prestamos es modificada si el préstamo es encontrado y se imprime un mensaje de actualización.
    """
    actualizar_prestamo(prestamos, id_prestamo, nuevo_estado='devuelto')



