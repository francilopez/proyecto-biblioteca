### PRIMERA APROXIMACIÓN DEL CODIGO PARA GESTION DE PRESTAMOS
##Gestión de Préstamos 
# o Registrar préstamos de libros a los clientes.
# o Leer y visualizar el historial de préstamos. 
# o Actualizar la información de los préstamos (fechas, estado). 
# o Registrar la devolución de libros y actualizar el estado del préstamo. 

import datetime

# Lista para almacenar los préstamos
prestamos = []

def agregar_prestamo(id_prestamo, id_libro, id_cliente, fecha_prestamo):
    """ Agrega un nuevo préstamo a la lista de préstamos """
    prestamos.append({
        'id': id_prestamo,
        'id_libro': id_libro,
        'id_cliente': id_cliente,
        'fecha_prestamo': fecha_prestamo,
        'estado': 'prestado'  # Estado inicial del préstamo
    })
    print(f"Préstamo agregado: ID={id_prestamo}, Libro ID={id_libro}, Cliente ID={id_cliente}, Fecha={fecha_prestamo}")

def listar_prestamos():
    """ Lista todos los préstamos actuales """
    if prestamos:
        print("Historial de Préstamos:")
        [print(f"ID: {prestamo['id']}, Libro ID: {prestamo['id_libro']}, Cliente ID: {prestamo['id_cliente']}, Fecha de Préstamo: {prestamo['fecha_prestamo']}, Estado: {prestamo['estado']}") for prestamo in prestamos]
    else:
        print("No hay préstamos actuales.")

def actualizar_prestamo(id_prestamo, nueva_fecha=None, nuevo_estado=None):
    """ Actualiza la información del préstamo especificado """
    global prestamos
    prestamos = [
        {**p, 'fecha_prestamo': nueva_fecha if p['id'] == id_prestamo and nueva_fecha else p['fecha_prestamo'],
         'estado': nuevo_estado if p['id'] == id_prestamo and nuevo_estado else p['estado']}
        for p in prestamos
    ]
    # Verificar si el préstamo fue actualizado
    prestamo_actualizado = next((p for p in prestamos if p['id'] == id_prestamo), None)
    if prestamo_actualizado:
        print(f"Préstamo con ID={id_prestamo} actualizado: Fecha={prestamo_actualizado['fecha_prestamo']}, Estado={prestamo_actualizado['estado']}")
    else:
        print(f"No se encontró el préstamo con ID={id_prestamo}")

def registrar_devolucion(id_prestamo):
    """ Registra la devolución de un libro y actualiza el estado del préstamo """
    actualizar_prestamo(id_prestamo, nuevo_estado='devuelto')
