from gestion_usuarios import imprimir_matriz_usuarios, eliminar_usuario, agregar_usuario, editar_usuario
from gestion_libros import agregar_libro, mostrar_libros, actualizar_libro, eliminar_libro, ordenar_libros
from gestion_prestamos import agregar_prestamo, listar_prestamos, actualizar_prestamo, registrar_devolucion
from busqueda import busquedaLibros
import sys

matriz_usuarios = [
    [1, "francisco", "francilopez@uade.edu.ar", "21/12/2003"],
    [2, "valentin", "valentin@uade.edu.ar", "16/10/2003"],
    [3, "gonzalo", "gonzalo12@gmail.com", "27/01/2002"],
    [4, "sofia", "sofia2@gmail.com", "09/12/2010"],
    [5, "ciro", "ciro@gmail.com", "11/01/1988"],
    [6, "valentina", "valentina2@hotmail.com", "21/09/2000"]
]

libros = [
    [201, 'Sherlock Holmes', 'ABC'],
    [202, 'El Gran Gatsby', 'Planeta'],
    [203, 'Harry Potter', 'Planeta'],
    [204, 'Frankenstein', 'Alfaguara'],
    [205, 'Los Juegos del Hambre', 'Penguin Random House'],
    [206, 'Cien Años de Soledad', 'ABC']
]

prestamos = [
    {'id': 1, 'id_libro': 201, 'id_cliente': 1, 'fecha_prestamo': '2024-08-01', 'estado': 'prestado'},
    {'id': 2, 'id_libro': 202, 'id_cliente': 2, 'fecha_prestamo': '2024-08-02', 'estado': 'devuelto'},
    {'id': 3, 'id_libro': 203, 'id_cliente': 3, 'fecha_prestamo': '2024-08-03', 'estado': 'retrasado'},
    {'id': 4, 'id_libro': 204, 'id_cliente': 4, 'fecha_prestamo': '2024-08-04', 'estado': 'prestado'},
    {'id': 5, 'id_libro': 205, 'id_cliente': 5, 'fecha_prestamo': '2024-08-05', 'estado': 'devuelto'},
    {'id': 6, 'id_libro': 206, 'id_cliente': 6, 'fecha_prestamo': '2024-08-06', 'estado': 'prestado'},
]

def menu_usuarios():
    """
Pre: matriz_usuarios debe estar definida y ser accesible. Las funciones imprimir_matriz_usuarios, agregar_usuario, eliminar_usuario, editar_usuario, y menu deben estar definidas. El valor ingresado para opcion debe ser un número entero.
Pos: Dependiendo de la opción seleccionada, la función ejecuta una acción correspondiente (mostrar, agregar, eliminar, editar usuarios, o regresar al menú principal). Si se ingresa una opción no válida, se mostrará un mensaje de error. El menú continuará mostrándose en un bucle hasta que se seleccione la opción para regresar al menú principal o el programa se detenga.
    """
    while True:
        print("Gestion de usuarios: Seleccione la opcion que desea ejecutar. ")
        print("1. Mostrar matriz de usuarios.")
        print("2. Agregar usuario a la matriz.")
        print("3. Eliminar usuario de la matriz.")
        print("4. Editar datos de un usuario.")
        print("5. Regresar al menu principal.")

        opcion = int(input("Opcion: "))

        if opcion == 1:
            imprimir_matriz_usuarios(matriz_usuarios)
        elif opcion == 2:
            agregar_usuario(matriz_usuarios)
        elif opcion == 3:
            try:
                user_id = int(input("Ingrese el ID del usuario a eliminar: "))
                eliminar_usuario(matriz_usuarios, user_id)
            except ValueError:
                print("ID inválido. Debe ser un número entero.")
        elif opcion == 4:
            editar_usuario(matriz_usuarios)
        elif opcion == 5:
            menu()
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")

def menu_libros():
    """
Pre: libros debe estar definida y ser accesible. Las funciones mostrar_libros, agregar_libro, actualizar_libro, eliminar_libro, ordenar_libros, y menu deben estar definidas. El valor ingresado para opcion debe ser un número entero.
Pos: Dependiendo de la opción seleccionada, la función ejecuta la acción correspondiente (mostrar, agregar, actualizar, eliminar libros, ordenar la lista, o regresar al menú principal). Si se ingresa una opción no válida, se mostrará un mensaje de error. El menú continuará mostrándose en un bucle hasta que se seleccione la opción para regresar al menú principal o el programa se detenga.
    """
    while True:
        print("\nGestion de libros: Seleccione la opcion que desea ejecutar. ")
        print("1. Mostrar matriz de libros.")
        print("2. Agregar un libro a la matriz.")
        print("3. Actualizar datos de un libro.")
        print("4. Eliminar un libro de la matriz.")
        print("5. Ordenar matriz de libros por nombre.")
        print("6. Regresar al menu principal.")

        opcion = int(input("Opcion: "))

        if opcion == 1:
            mostrar_libros(libros)
        elif opcion == 2:
            try:
                id_libro = int(input("Ingrese el ID del nuevo libro: "))
                nombre = input("Ingrese el nombre del nuevo libro: ")
                editorial = input("Ingrese la editorial del nuevo libro: ")
                agregar_libro(libros, id_libro, nombre, editorial)
            except ValueError:
                print("ID inválido. Debe ser un número entero.")
        elif opcion == 3:
            try:
                id_libro = int(input("Ingrese el ID del libro a actualizar: "))
                nuevo_nombre = input("Ingrese el nuevo nombre del libro (deje en blanco para no cambiar): ")
                nueva_editorial = input("Ingrese la nueva editorial del libro (deje en blanco para no cambiar): ")
                actualizar_libro(libros, id_libro, nuevo_nombre or None, nueva_editorial or None)
            except ValueError:
                print("ID inválido. Debe ser un número entero.")   
        elif opcion == 4:
             try:
                id_libro = int(input("Ingrese el ID del libro a eliminar: "))
                eliminar_libro(libros, id_libro)
             except ValueError:
                print("ID inválido. Debe ser un número entero.")
        elif opcion == 5:
                ordenar_libros(libros)
        elif opcion == 6:
            menu()
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 6.")


def menu_prestamos():
    """
Pre: prestamos debe estar definido y ser accesible. Las funciones listar_prestamos, agregar_prestamo, registrar_devolucion, y menu deben estar definidas. El valor ingresado para opcion debe ser un número entero.
Pos: Dependiendo de la opción seleccionada, la función ejecutará la acción correspondiente (listar, agregar, registrar devolución de préstamos, o regresar al menú principal). Si se ingresa una opción no válida, se mostrará un mensaje de error. El menú continuará mostrándose en un bucle hasta que se seleccione la opción para regresar al menú principal o el programa se detenga.
    """
    while True:
        print("\nGestion de prestamos: Seleccione la opcion que desea ejecutar. ")
        print("1. Listar prestamos.")
        print("2. Agregar un prestamo.")
        print("3. Registrar devolucion.")
        print("4. Regresar al menu principal.")

        opcion = int(input("Opcion: "))

        if opcion == 1:
            listar_prestamos(prestamos)
        elif opcion == 2:
            try:
                id_prestamo = int(input("Ingrese el ID del nuevo préstamo: "))
                id_libro = int(input("Ingrese el ID del libro a prestar: "))
                id_cliente = int(input("Ingrese el ID del cliente: "))
                fecha_prestamo = input("Ingrese la fecha de préstamo (YYYY-MM-DD): ")
                agregar_prestamo(prestamos, id_prestamo, id_libro, id_cliente, fecha_prestamo)
            except ValueError:
                print("ID inválido. Debe ser un número entero.")
        elif opcion == 3:
            try:
                id_prestamo = int(input("Ingrese el ID del préstamo a devolver: "))
                registrar_devolucion(prestamos, id_prestamo)
            except ValueError:
                print("ID inválido. Debe ser un número entero.")
        elif opcion == 4:
            menu()
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")


#menu()

#BUSQUEDA DE LIBRO buscar_libros_interactivo(biblioteca) # Esto va en el main

def menu():
    """
Pre: Las funciones menu_usuarios(), menu_libros(), menu_prestamos(), y busquedaLibros(libros) estan definidas y tienen que funcionar correctamente. libros debe estar definido y accesible. El módulo sys debe estar importado. El valor ingresado para opcion debe ser un número entero.
Pos: Dependiendo de la opción seleccionada, el menú llamará a la función correspondiente para gestionar usuarios, libros, préstamos, o realizar una búsqueda. Si se selecciona la opción 5, el programa se terminará. Si se ingresa una opción no válida, se mostrará un mensaje de error y el menú continuará mostrando las opciones hasta que el programa se detenga o se seleccione la opción de salir.
    """
    while True:
        print("\nIngrese el número correspondiente a la opción que desea ejecutar: ")
        print("1. Gestion de usuarios.")
        print("2. Gestion de libros.")
        print("3. Gestion de prestamos.")
        print("4. Busqueda de libros.")
        print("5. Salir del programa")

        opcion= int(input("Opcion: "))

        if opcion == 1:
            menu_usuarios()
        elif opcion == 2:
            menu_libros()
        elif opcion == 3:
            menu_prestamos()
        elif opcion == 4:
            busquedaLibros(libros)
        elif opcion == 5:
            print("Saliendo del programa...")
            sys.exit()
        else:
            print("Opcion no valida. Por favor, seleccione una opcion del 1 al 5.")

menu()
