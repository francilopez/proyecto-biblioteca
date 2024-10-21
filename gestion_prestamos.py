import datetime


def agregar_prestamo(prestamos, id_prestamo, id_libro, id_cliente, fecha_prestamo):
    """Agrega un nuevo préstamo a la lista de préstamos."""
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
    """Lista todos los préstamos actuales."""
    if not prestamos:
        print("No hay préstamos actuales.")
    else:
        print("Historial de Préstamos:")
        for prestamo in prestamos:
            print(f"ID: {prestamo['id']}, Libro ID: {prestamo['id_libro']}, Cliente ID: {prestamo['id_cliente']}, Fecha de Préstamo: {prestamo['fecha_prestamo']}, Estado: {prestamo['estado']}")

def actualizar_prestamo(prestamos, id_prestamo, nueva_fecha=None, nuevo_estado=None):
    """Actualiza la información del préstamo especificado."""
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
    """Registra la devolución de un libro y actualiza el estado del préstamo."""
    actualizar_prestamo(prestamos, id_prestamo, nuevo_estado='devuelto')



