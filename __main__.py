from gestion_usuarios import imprimir_matriz_usuarios, eliminar_usuario, agregar_usuario, editar_usuario

matriz_usuarios = [
    [1, "francisco", "francilopez@uade.edu.ar", "21/12/2003"],
    [2, "valentin", "valentin@uade.edu.ar", "16/10/2003"],
    [3, "gonzalo", "gonzalo12@gmail.com", "27/01/2002"],
    [4, "sofia", "sofia2@gmail.com", "09/12/2010"],
    [5, "ciro", "ciro@gmail.com", "11/01/1988"],
    [6, "valentina", "valentina2@hotmail.com", "21/09/2000"]
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
        print("9. Lista de prestamos de la biblioteca.")
        print("10. Pedir un prestamo a la biblioteca.")
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
            editar_usuario(matriz_usuarios)
        elif option == '5':
            mostrar_biblioteca(biblioteca)
        elif option == '6':
            agregar_libro(biblioteca)
        elif option == '7':
             try:
                id_libro = int(input("Ingrese el ID del libro a eliminar: "))
                eliminar_libro(biblioteca, id_libro)
            except ValueError:
                print("ID inválido. Debe ser un número entero.")
        elif opcion == '12':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 12.")
