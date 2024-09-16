def mostrar_libros(libros):
    """Muestra todos los libros en la lista."""
    if not libros:
        print("La lista de libros está vacía.")
    else:
        for libro in libros:
            print(f"ID: {libro[0]}, Nombre: {libro[1]}, Editorial: {libro[2]}")

def agregar_libro(libros, id_libro, nombre, editorial):
    """Agrega un nuevo libro a la lista de libros."""
    # Verifica si el libro con el mismo ID ya existe
    for libro in libros:
        if libro[0] == id_libro:
            print(f"El libro con ID {id_libro} ya existe.")
            return
    nuevo_libro = [id_libro, nombre, editorial]
    libros.append(nuevo_libro)
    print(f"Libro con ID {id_libro} añadido exitosamente.")

def actualizar_libro(libros, id_libro, nombre=None, editorial=None):
    """Actualiza los datos de un libro existente en la lista."""
    for libro in libros:
        if libro[0] == id_libro:
            if nombre:
                libro[1] = nombre
            if editorial:
                libro[2] = editorial
            print(f"Libro con ID {id_libro} actualizado exitosamente.")
            return
    print(f"No se encontró un libro con ID {id_libro}.")

def eliminar_libro(libros, id_libro):
    """Elimina un libro existente en la lista por su ID."""
    for i, libro in enumerate(libros):
        if libro[0] == id_libro:
            del libros[i]
            print(f"Libro con ID {id_libro} eliminado exitosamente.")
            return
    print(f"No se encontró un libro con ID {id_libro}.")

def ordenar_libros(libros):
    """Ordena la lista de libros por nombre del libro."""
    libros.sort(key=lambda libro: libro[1])  # Cambiado de libro.nombre a libro[1]
    print("Libros ordenados exitosamente.")
