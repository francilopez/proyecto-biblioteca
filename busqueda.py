def busquedaLibros(biblioteca):
    
    # solicitar al usuario
    print("Criterios de búsqueda disponibles: ")
    print("1 - Buscar por ID")
    print("2 - Buscar por Nombre")
    print("3 - Buscar por Editorial")
    
    criterio = input("Seleccione el criterio de busqueda (1, 2, 3): ")
    
    # verifica que sea válido
    if criterio not in ['1', '2', '3']:
        print("Criterio no válido. Intente nuevamente.")
        return
    
    # valor que el usuario quiere buscar
    valor = input("Ingrese el valor a buscar: ")
    
    #limitar o no los resultados
    nResultados = input("¿Cuántos resultados quiere mostrar? (Deje en blanco para mostrar todos): ")
    nResultados = int(nResultados) if nResultados else None
    
    # busqueda según el criterio seleccionado
    criterio = int(criterio) - 1 
    resultados = list(filter(lambda libro: valor.lower() in libro[criterio].lower(), biblioteca))
    
    # slicing si se aclara el iímite
    if nResultados:
        resultados = resultados[:nResultados]
    
    if resultados:
        print("\nResultados encontrados:")
        for libro in resultados:
            print(f"ID: {libro[0]}, Nombre: {libro[1]}, Editorial: {libro[2]}")
    else:
        print(f"No se encontraron libros que coincidan con '{valor}'.")

print("¡Bienvenido a la biblioteca!\n")
