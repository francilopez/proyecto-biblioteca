def leer_desde_txt_libros(archivos):
    """Carga los libros desde un archivo de texto."""
    libros = []  # Cambié "libro" por "libros"
    ids = set()  # Este conjunto podría ser útil más adelante si necesitas verificar si un ID ya existe.
    try:
        with open(archivos, 'r') as f:
            for linea in f:
                datos = linea.strip().split(',')
                if len(datos) >= 3:  # Asegurarse de que la línea tiene al menos 3 elementos
                    id_libro = int(datos[0])  # Convertimos el ID a entero
                    nombre = datos[1]
                    editorial = datos[2]
                    libros.append([id_libro, nombre, editorial])
                    ids.add(id_libro)  # Añadimos el ID al conjunto para evitar duplicados
                else:
                    print(f"Advertencia: La línea no tiene suficientes datos: {linea.strip()}")
        print(f"Libros cargados desde {archivos} exitosamente.")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
    
    return libros, ids


def guardar_en_txt_libros(libros, archivos):
    """Guarda la lista de libros en un archivo de texto."""
    try:
        with open(archivos, 'w') as f:
            for libro in libros:
                linea = f"{libro[0]},{libro[1]},{libro[2]}\n"
                f.write(linea)
        print(f"Libros guardados en {archivos} exitosamente.")
    except Exception as e:
        print(f"Error al guardar en el archivo: {e}")

def mostrar_libros(libros):
    """Muestra todos los libros en la lista."""
    if not libros:
        print("La lista de libros está vacía.")
    else:
        print(f"{'ID':<5} {'Nombre':<30} {'Editorial':<20}")
        print("-" * 65) 
        for libro in libros:
            print(f"{libro[0]:<5} {libro[1]:<30} {libro[2]:<20}")

def agregar_libro(libros, ids, id_libro, nombre, editorial):
    """Agrega un nuevo libro a la lista de libros."""
    if id_libro in ids:
        print(f"El libro con ID {id_libro} ya existe.")
        return
    nuevo_libro = [id_libro, nombre, editorial]
    libros.append(nuevo_libro)
    ids.add(id_libro)
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

def eliminar_libro(libros, ids, id_libro):
    """Elimina un libro existente en la lista por su ID."""
    for i, libro in enumerate(libros):
        if libro[0] == id_libro:
            del libros[i]
            ids.remove(id_libro)
            print(f"Libro con ID {id_libro} eliminado exitosamente.")
            return
    print(f"No se encontró un libro con ID {id_libro}.")

def ordenar_libros(libros):
    """Ordena la lista de libros por nombre del libro."""
    libros.sort(key=lambda libro: libro[1])
    print("Libros ordenados exitosamente.")
    

###### USO DE RECURSIVIDAD PARA ORDENAR FIJARSE SI PONERLO ACA ####

def ordenar_libros(libros):
    """Ordena la lista de libros por nombre del libro de forma recursiva."""
    def ordenar_recursivo(libros, idx=1):
        if idx >= len(libros):  # Caso base: si ya hemos recorrido toda la lista
            return
        for i in range(idx, len(libros)):
            if libros[i][1] < libros[idx - 1][1]:
                libros[i], libros[idx - 1] = libros[idx - 1], libros[i]
        ordenar_recursivo(libros, idx + 1)  # Llamada recursiva para ordenar el siguiente libro
    
    ordenar_recursivo(libros)
    print("Libros ordenados exitosamente.")
