from gestion_usuarios import imprimir_matriz_usuarios, eliminar_usuario, agregar_usuario, editar_usuario,leer_desde_txt, guardar_en_txt
from gestion_libros import agregar_libro, mostrar_libros, actualizar_libro, eliminar_libro, ordenar_libros, leer_desde_txt_libros,guardar_en_txt_libros
from gestion_prestamos import cargar_prestamos, guardar_prestamos, agregar_prestamo, listar_prestamos, actualizar_prestamo, registrar_devolucion
from busqueda import busquedaLibros
import json

archivo = 'usuarios.txt'
matriz_usuarios = leer_desde_txt(archivo)


archivo_libros = 'libros.txt'


# prestamos = [
#     {'id': 1, 'id_libro': 201, 'id_cliente': 1, 'fecha_prestamo': '2024-08-01', 'estado': 'prestado'},
#     {'id': 2, 'id_libro': 202, 'id_cliente': 2, 'fecha_prestamo': '2024-08-02', 'estado': 'devuelto'},
#     {'id': 3, 'id_libro': 203, 'id_cliente': 3, 'fecha_prestamo': '2024-08-03', 'estado': 'retrasado'},
#     {'id': 4, 'id_libro': 204, 'id_cliente': 4, 'fecha_prestamo': '2024-08-04', 'estado': 'prestado'},
#     {'id': 5, 'id_libro': 205, 'id_cliente': 5, 'fecha_prestamo': '2024-08-05', 'estado': 'devuelto'},
#     {'id': 6, 'id_libro': 206, 'id_cliente': 6, 'fecha_prestamo': '2024-08-06', 'estado': 'prestado'},
# ]
# with open('prestamos.json', 'w') as file:
#     json.dump(prestamos, file, indent=4)

prestamos = cargar_prestamos('prestamos.json')

def menu_usuarios():
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
            guardar_en_txt(matriz_usuarios, archivo)
        elif opcion == 3:
            try:
                user_id = int(input("Ingrese el ID del usuario a eliminar: "))
                eliminar_usuario(matriz_usuarios, user_id)
                guardar_en_txt(matriz_usuarios,archivo)
            except ValueError:
                print("ID inválido. Debe ser un número entero.")
        elif opcion == 4:
            editar_usuario(matriz_usuarios)
            guardar_en_txt(matriz_usuarios,archivo)
        elif opcion == 5:
            guardar_en_txt(matriz_usuarios, archivo)
            return
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")

def menu_libros():
    libros, ids = leer_desde_txt_libros(archivo_libros)
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
                agregar_libro(libros,ids, id_libro, nombre, editorial)
                guardar_en_txt_libros(libros, archivo_libros)
            except ValueError:
                print("ID inválido. Debe ser un número entero.")
        elif opcion == 3:
            try:
                id_libro = int(input("Ingrese el ID del libro a actualizar: "))
                nuevo_nombre = input("Ingrese el nuevo nombre del libro (deje en blanco para no cambiar): ")
                nueva_editorial = input("Ingrese la nueva editorial del libro (deje en blanco para no cambiar): ")
                actualizar_libro(libros,archivo_libros, id_libro, nuevo_nombre or None, nueva_editorial or None)
                guardar_en_txt_libros(libros, archivo_libros)
            except ValueError:
                print("ID inválido. Debe ser un número entero.")   
        elif opcion == 4:
             try:
                id_libro = int(input("Ingrese el ID del libro a eliminar: "))
                eliminar_libro(libros,ids,archivo_libros, id_libro)
                guardar_en_txt_libros(libros, archivo_libros)
             except ValueError:
                print("ID inválido. Debe ser un número entero.")
        elif opcion == 5:
                ordenar_libros(libros, archivo_libros)
        elif opcion == 6:
            return
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 6.")


def menu_prestamos():
    archivo_prestamos = 'prestamos.json'
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
                agregar_prestamo(prestamos, archivo_prestamos, id_prestamo, id_libro, id_cliente, fecha_prestamo)
            except ValueError:
                print("ID inválido. Debe ser un número entero.")
        elif opcion == 3:
            try:
                id_prestamo = int(input("Ingrese el ID del préstamo a devolver: "))
                registrar_devolucion(prestamos,archivo_prestamos, id_prestamo)
            except ValueError:
                print("ID inválido. Debe ser un número entero.")
        elif opcion == 4:
            return
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")


def menu():
    opcion = 0

    while opcion != 5:
        print("\nIngrese el número correspondiente a la opción que desea ejecutar: ")
        print("1. Gestion de usuarios.")
        print("2. Gestion de libros.")
        print("3. Gestion de prestamos.")
        print("4. Busqueda de libros.")
        print("5. Salir del programa")
        

        try:
            opcion = int(input("Opcion: "))
        except ValueError:
            print("por favor, ingrese una opcion valida.")
            continue   

        if opcion == 1:
            menu_usuarios()
        elif opcion == 2:
            menu_libros()
        elif opcion == 3:
            menu_prestamos()
        elif opcion == 4:
            libros, ids = leer_desde_txt_libros(archivo_libros)
            busquedaLibros(libros)
        elif opcion == 5:
            print("Saliendo del programa...")
        else:
            print("Opcion no valida. Por favor, seleccione una opcion del 1 al 5.")
menu()
