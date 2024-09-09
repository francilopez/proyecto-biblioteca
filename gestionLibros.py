# Definimos la biblioteca como una lista vacía
biblioteca = []

def agregar_libro(biblioteca, id_libro, nombre, editorial):
    """Agrega un nuevo libro a la biblioteca."""
    # Verifica si el libro con el mismo ID ya existe
    for libro in biblioteca:
        if libro[0] == id_libro:
            print(f"El libro con ID {id_libro} ya existe.")
            return
    nuevo_libro = [id_libro, nombre, editorial]
    biblioteca.append(nuevo_libro)
    print(f"Libro con ID {id_libro} añadido exitosamente.")  

def mostrar_biblioteca(biblioteca):
    """Muestra todos los libros en la biblioteca."""
    if not biblioteca:
        print("La biblioteca está vacía.")
    for libro in biblioteca:
        print(f"ID: {libro[0]}, Nombre: {libro[1]}, Editorial: {libro[2]}")

def actualizar_libro(biblioteca, id_libro, nombre=None, editorial=None):
    """Actualiza los datos de un libro existente en la biblioteca."""
    for libro in biblioteca:
        if libro[0] == id_libro:
            if nombre:
                libro[1] = nombre
            if editorial:
                libro[2] = editorial
            print(f"Libro con ID {id_libro} actualizado exitosamente.")
            return
    print(f"No se encontró un libro con ID {id_libro}.")

def eliminar_libro(biblioteca, id_libro):
    """Elimina un libro existente en la biblioteca por su ID."""
    for i, libro in enumerate(biblioteca):
        if libro[0] == id_libro:
            del biblioteca[i]
            print(f"Libro con ID {id_libro} eliminado exitosamente.")
            return
    print(f"No se encontró un libro con ID {id_libro}.")


# Ejemplo de uso
agregar_libro(biblioteca, 1, 'Sherlock Holmes', 'ABC')
agregar_libro(biblioteca, 2, 'El Gran Gatsby', 'Planeta')
agregar_libro(biblioteca, 3 , 'Harry Potter', 'Planeta')
agregar_libro(biblioteca, 4, 'Frankenstein', 'Alfaguara')

# Mostrar todos los libros en la biblioteca
mostrar_biblioteca(biblioteca)

# Actualizar un libro
actualizar_libro(biblioteca, 1, nombre='Sherlock Holmes (Edición Especial)', editorial='Urano')

# Mostrar todos los libros en la biblioteca después de la actualización
mostrar_biblioteca(biblioteca)

# Eliminar un libro
eliminar_libro(biblioteca, 2)

# Mostrar todos los libros en la biblioteca después de la eliminación
mostrar_biblioteca(biblioteca)