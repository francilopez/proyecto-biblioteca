import json
import os

def cargar_prestamos(filename):
    """Carga los préstamos desde un archivo JSON."""
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []

def guardar_prestamos(prestamos, filename):
    """Guarda los préstamos en un archivo JSON."""
    with open(filename, 'w') as file:
        json.dump(prestamos, file, indent=4)

def agregar_prestamo(prestamos, filename, id_prestamo, id_libro, id_cliente, fecha_prestamo):
    """Agrega un nuevo préstamo a la lista de préstamos."""
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
    guardar_prestamos(prestamos, filename)  # Guardar cambios
    print(f"Préstamo agregado: ID={id_prestamo}, Libro ID={id_libro}, Cliente ID={id_cliente}, Fecha={fecha_prestamo}")

def listar_prestamos(prestamos):
    """Lista todos los préstamos actuales."""
    if not prestamos:
        print("No hay préstamos actuales.")
    else:
        print("Historial de Préstamos:")
        for prestamo in prestamos:
            print(f"ID: {prestamo['id']}, Libro ID: {prestamo['id_libro']}, Cliente ID: {prestamo['id_cliente']}, Fecha de Préstamo: {prestamo['fecha_prestamo']}, Estado: {prestamo['estado']}")

def actualizar_prestamo(prestamos, filename, id_prestamo, nueva_fecha=None, nuevo_estado=None):
    """Actualiza la información del préstamo especificado."""
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
    """Registra la devolución de un libro y actualiza el estado del préstamo."""
    actualizar_prestamo(prestamos, filename, id_prestamo, nuevo_estado='devuelto')
