def mostrar_libros(libros):
    """
    Precondiciones: libros debe ser una lista de iterables con exactamente tres elementos.
    Poscondiciones: imprimirá un mensaje si la lista está vacía o imprimirá la información de cada libro si la lista contiene elementos.
    """
    if not libros:
        print("La lista de libros está vacía.")
    else:
        for libro in libros:
            print(f"ID: {libro[0]}, Nombre: {libro[1]}, Editorial: {libro[2]}")

def agregar_libro(libros, id_libro, nombre, editorial):
    """
    Pre: libros debe ser una lista de listas que contiene libros con tres elementos id_libro, nombre y editorial.
    Pos: Si el ID del libro ya existe, imprime un mensaje de error. Si el ID es único, se añade el libro a la lista.
    """
    for libro in libros:
        if libro[0] == id_libro:
            print(f"El libro con ID {id_libro} ya existe.")
            return
    nuevo_libro = [id_libro, nombre, editorial]
    libros.append(nuevo_libro)
    print(f"Libro con ID {id_libro} añadido exitosamente.")

def actualizar_libro(libros, id_libro, nombre=None, editorial=None):
    """
Pre: libros debe ser una lista de listas con tres elementos id_libro, nombre y editorial.
Pos: Si el ID del libro existe, los campos especificados se actualizan y se imprime un mensaje de éxito. Si el ID no existe, se imprime un mensaje de que el libro no fue encontrado.
    """
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
    """
Pre: libros debe ser una lista de listas que debe tener elementos en la lista, id_libro debe ser comparable con el primer elemento de esos elementos.
Poscondiciones: Si el libro con el ID proporcionado existe en la lista, se elimina y se imprime un mensaje de éxito. Si el libro no se encuentra, se imprime un mensaje diciendo que no fue encontrado y la lista permanece sin cambios.
    """
    for i, libro in enumerate(libros):
        if libro[0] == id_libro:
            del libros[i]
            print(f"Libro con ID {id_libro} eliminado exitosamente.")
            return
    print(f"No se encontró un libro con ID {id_libro}.")

def ordenar_libros(libros):
    """
Pre: libros debe ser una lista de listas con al menos dos elementos, donde el segundo elemento es una cadena que representa el nombre del libro.
Pos: La lista libros es ordenada en orden alfabético basado en los nombres de los libros (libro[1]), y se imprime un mensaje indicando que se realizó exitosamente.
    """
    libros.sort(key=lambda libro: libro[1])  # Cambiado de libro.nombre a libro[1]
    print("Libros ordenados exitosamente.")

