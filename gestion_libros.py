def leer_desde_txt_libros(archivo_libros):
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
    try:
        with open(archivo_libros, 'w') as f:
            for libro in libros:
                linea = f"{libro[0]},{libro[1]},{libro[2]}\n"
                f.write(linea)
        print(f"Libros guardados en {archivo_libros} exitosamente.")
    except Exception as e:
        print(f"Error al guardar en el archivo {archivo_libros}: {e}")






def mostrar_libros(libros):
    if not libros:
        print("La lista de libros está vacía.")
    else:
        print(f"{'ID':<5} {'Nombre':<30} {'Editorial':<20}")
        print("-" * 65)
        for libro in libros:
            print(f"{libro[0]:<5} {libro[1]:<30} {libro[2]:<20}")





def agregar_libro(libros, ids, id_libro, nombre, editorial):
    if id_libro in ids:
        print(f"El libro con ID {id_libro} ya existe.")
        return
    nuevo_libro = [id_libro, nombre, editorial]
    libros.append(nuevo_libro)
    ids.add(id_libro)
    print(f"Libro con ID {id_libro} añadido exitosamente.")






def actualizar_libro(libros, archivo_libros, id_libro, nombre=None, editorial=None):
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
    for i, libro in enumerate(libros):
        if libro[0] == id_libro:
            del libros[i]
            ids.remove(id_libro)
            guardar_en_txt_libros(libros, archivo_libros)
            print(f"Libro con ID {id_libro} eliminado exitosamente.")
            return
    print(f"No se encontró un libro con ID {id_libro}.")






def ordenar_libros(libros, archivo_libros):
    libros.sort(key=lambda libro: libro[1])
    guardar_en_txt_libros(libros, archivo_libros)
    print("Libros ordenados exitosamente.")






###### USO DE RECURSIVIDAD PARA ORDENAR FIJARSE SI PONERLO ACA ####

# def ordenar_libros(libros):
#     """Ordena la lista de libros por nombre del libro de forma recursiva."""
#     def ordenar_recursivo(libros, idx=1):
#         if idx >= len(libros):  # Caso base: si ya hemos recorrido toda la lista
#             return
#         for i in range(idx, len(libros)):
#             if libros[i][1] < libros[idx - 1][1]:
#                 libros[i], libros[idx - 1] = libros[idx - 1], libros[i]
#         ordenar_recursivo(libros, idx + 1)  # Llamada recursiva para ordenar el siguiente libro
    
#     ordenar_recursivo(libros)
#     print("Libros ordenados exitosamente.")

### ESTA SERIA LA MEJOR OPCION DE RECURSIVIDAD
# def mostrar_libros(libros):
#     """Muestra todos los libros en la lista de forma recursiva."""
#     def mostrar_recursivamente(libros, idx=0):
#         if idx >= len(libros):  # Caso base: si el índice es mayor que el tamaño de la lista
#             return
#         libro = libros[idx]
#         print(f"{str(libro[0]):<5} {str(libro[1]):<30} {str(libro[2]):<20}")
#         mostrar_recursivamente(libros, idx + 1)  # Llamada recursiva para mostrar el siguiente libro
    
#     if not libros:
#         print("La lista de libros está vacía.")
#     else:
#         print(f"{'ID':<5} {'Nombre':<30} {'Editorial':<20}")
#         print("-" * 65)
#         mostrar_recursivamente(libros)
