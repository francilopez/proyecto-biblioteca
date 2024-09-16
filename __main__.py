from gestion_usuarios import imprimir_matriz_usuarios, eliminar_usuario, agregar_usuario, editar_usuario, cambiar_datos
from gestion_libros import agregar_libro, mostrar_libros, actualizar_libro, eliminar_libro, ordenar_libros
from gestion_prestamos import agregar_prestamo, listar_prestamos, actualizar_prestamo, registrar_devolucion

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

def menu():
    while True:
        print("\nIngrese el número correspondiente a la opción que desea ejecutar: ")
        print("1. Mostrar matriz de usuarios.")
        print("2. Agregar usuarios a la matriz.")
        print("3. Eliminar usuarios de la matriz.")
        print("4. Editar datos de un usuario.")
        print("5. Mostrar biblioteca.")
        print("6. Agregar libro a la biblioteca.")
        print("7. Eliminar libro de la biblioteca.")
        print("8. Actualizar la biblioteca.")
        print("9. Lista de préstamos de la biblioteca.")
        print("10. Pedir un préstamo a la biblioteca.")
        print("11. Registrar la devolución de un libro.")
        print("12. Salir.")

        opcion = input("Opción: ")
        
        if opcion == '1':
            imprimir_matriz_usuarios(matriz_usuarios)
        elif opcion == '2':
            agregar_usuario(matriz_usuarios)
        elif opcion == '3':
            try:
                user_id = int(input("Ingrese el ID del usuario a eliminar: "))
                eliminar_usuario(matriz_usuarios, user_id)
            except ValueError:
                print("ID inválido. Debe ser un número entero.")
        elif opcion == '4':
            cambiar_datos(matriz_usuarios)
        elif opcion == '5':
            mostrar_libros(libros)
        elif opcion == '6':
            try:
                id_libro = int(input("Ingrese el ID del nuevo libro: "))
                nombre = input("Ingrese el nombre del nuevo libro: ")
                editorial = input("Ingrese la editorial del nuevo libro: ")
                agregar_libro(libros, id_libro, nombre, editorial)
            except ValueError:
                print("ID inválido. Debe ser un número entero.")
        elif opcion == '7':
            try:
                id_libro = int(input("Ingrese el ID del libro a eliminar: "))
                eliminar_libro(libros, id_libro)
            except ValueError:
                print("ID inválido. Debe ser un número entero.")
        elif opcion == '8':
            try:
                id_libro = int(input("Ingrese el ID del libro a actualizar: "))
                nuevo_nombre = input("Ingrese el nuevo nombre del libro (deje en blanco para no cambiar): ")
                nueva_editorial = input("Ingrese la nueva editorial del libro (deje en blanco para no cambiar): ")
                actualizar_libro(libros, id_libro, nuevo_nombre or None, nueva_editorial or None)
            except ValueError:
                print("ID inválido. Debe ser un número entero.")
        elif opcion == '9':
            listar_prestamos(prestamos)
        elif opcion == '10':
            try:
                id_prestamo = int(input("Ingrese el ID del nuevo préstamo: "))
                id_libro = int(input("Ingrese el ID del libro a prestar: "))
                id_cliente = int(input("Ingrese el ID del cliente: "))
                fecha_prestamo = input("Ingrese la fecha de préstamo (YYYY-MM-DD): ")
                agregar_prestamo(prestamos, id_prestamo, id_libro, id_cliente, fecha_prestamo)
            except ValueError:
                print("ID inválido. Debe ser un número entero.")
        elif opcion == '11':
            try:
                id_prestamo = int(input("Ingrese el ID del préstamo a devolver: "))
                registrar_devolucion(prestamos, id_prestamo)
            except ValueError:
                print("ID inválido. Debe ser un número entero.")
        elif opcion == '12':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 12.")

        buscar_libros_interactivo(libros) # Esto va en el main
            
            
