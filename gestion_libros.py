def leer_desde_txt_libros(archivo_libros):
   # pre: que el parámetro archivo_libros sea una cadena de texto que represente un archivo de texto existente, que contenga información de libros en formato CSV
   # pos: devuelve una lista de libros (libros), donde cada libro es una lista de tres elementos ID, nombre y editorial
    libros = []
    ids = set()
    try:
        with open(archivo_libros, 'r') as f:
            for linea in f:
                datos = linea.strip().split(',')
                datos[0] = int(datos[0])  # Convertir el ID a entero
                libros.append(datos)      # Añadir el libro a la lista
                ids.add(datos[0])         # Añadir el ID al conjunto de IDs
    except Exception as e:
        print(f"Error al leer el archivo {archivo_libros}: {e}")
    return libros, ids




def guardar_en_txt_libros(libros, archivo_libros):
    # pre: parámetro libros es una matriz, donde cada lista tiene al menos tres elementos ID, nombre y editorial, y que archivo_libros sea una ruta a un archivo de texto donde se almacenarán los libros.
    # pos: guarda la información de los libros en el archivo especificado por archivo_libros en formato CSV 
    try:
        with open(archivo_libros, 'w') as f:
            for libro in libros:
                linea = f"{libro[0]},{libro[1]},{libro[2]}\n"
                f.write(linea)
        print(f"Libros guardados en {archivo_libros} exitosamente.")
    except Exception as e:
        print(f"Error al guardar en el archivo {archivo_libros}: {e}")





def mostrar_libros(libros, idx=0):
    # pre: el parámetro libros es una matriz, donde cada lista contiene tres elementos: ID, nombre y editorial. idx es un índice que indica desde qué posición en la lista comenzar a mostrar los resultados
    # pos:  imprime los detalles de los libros (ID, nombre y editorial) en un formato tabular. Si el índice es mayor que el tamaño de la lista, la función termina.
    if not libros:
        print("La lista de libros está vacía.")
        return  # Si la lista está vacía, no hacer nada más.
    
    if idx >= len(libros):  # Caso base: si el índice es mayor que el tamaño de la lista
        return
    
    if idx == 0:  # Solo imprimir el encabezado una vez, cuando se comienza
        print(f"{'ID':<5} {'Nombre':<30} {'Editorial':<20}")
        print("-" * 65)

    libro = libros[idx]
    print(f"{str(libro[0]):<5} {str(libro[1]):<30} {str(libro[2]):<20}")
    mostrar_libros(libros, idx + 1)




def agregar_libro(libros, ids, id_libro, nombre, editorial):
    # pre: requiere que el parámetro libros sea una matriz, donde cada lista representa un libro con al menos tres elementos: ID, nombre y editorial.  ids debe ser un conjunto que contenga los IDs de los libros ya existentes.
    # pos: Si el id_libro no existe ya en el conjunto ids, la función agrega el nuevo libro a la lista libros y el id_libro al conjunto ids
    if id_libro in ids:
        print(f"El libro con ID {id_libro} ya existe.")
        return
    nuevo_libro = [id_libro, nombre, editorial]
    libros.append(nuevo_libro)
    ids.add(id_libro)
    print(f"Libro con ID {id_libro} añadido exitosamente.")






def actualizar_libro(libros, archivo_libros, id_libro, nombre=None, editorial=None):
    #pre: requiere que el parámetro libros sea una matriz, donde cada lista representa un libro con al menos tres elementos: ID, nombre y editorial. El parámetro id_libro debe ser un valor entero que representa el ID que se desea actualizar.
    #pos: Si se encuentra un libro con el id_libro en la lista libros, la función actualiza el nombre y/o la editorial del libro con los valores proporcionados y guarda la lista de libros actualizada en el archivo especificado.
    for libro in libros:
        if libro[0] == id_libro:
            if nombre:
                libro[1] = nombre
            if editorial:
                libro[2] = editorial
            guardar_en_txt_libros(libros, archivo_libros)
            print(f"Libro con ID {id_libro} actualizado exitosamente.")
            return
    print(f"No se encontró un libro con ID {id_libro}.")






def eliminar_libro(libros, ids, archivo_libros, id_libro):
    # pre: requiere que el parámetro libros sea una matriz, donde cada lista representa un libro con al menos tres elementos: ID, nombre y editorial. 
        # ids debe ser un conjunto que contiene los IDs de los libros. archivo_libros debe representar la ruta a un archivo donde se almacenan los libros.
    # pos: elimina el libro de la lista, remueve el id_libro del conjunto ids, guarda la lista de libros actualizada en el archivo especificado, y luego imprime un mensaje indicando que el libro se ha eliminado con éxito. 
    for i, libro in enumerate(libros):
        if libro[0] == id_libro:
            del libros[i]
            ids.remove(id_libro)
            guardar_en_txt_libros(libros, archivo_libros)
            print(f"Libro con ID {id_libro} eliminado exitosamente.")
            return
    print(f"No se encontró un libro con ID {id_libro}.")






def ordenar_libros(libros, archivo_libros):
    # pre: parámetro libros sea una matriz, donde cada lista representa un libro con al menos tres elementos: ID, nombre y editorial. archivo_libros debe representar la ruta a un archivo donde se guardarán los libros ordenados.
    # pos: ordena la lista libros alfabéticamente por el nombre del libro y luego guarda la lista de libros ordenada en el archivo especificado.
    libros.sort(key=lambda libro: libro[1])
    guardar_en_txt_libros(libros, archivo_libros)
    print("Libros ordenados exitosamente.")
