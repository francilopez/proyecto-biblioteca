matriz_usuarios = [
    [1, "francisco", "francilopez@uade.edu.ar", "21/12/2003"],
    [2, "valentin", "valentin@uade.edu.ar", "16/10/2003"],
    [3, "gonzalo", "gonzalo12@gmail.com", "27/01/2002"],
    [4, "sofia", "sofia2@gmail.com", "09/12/2010"],
    [5, "ciro", "ciro@gmail.com", "11/01/1988"],
    [6, "valentina", "valentina2@hotmail.com", "21/09/2000"]
]

def imprimir_matriz_usuarios(matriz):
    print(f"{'ID':<5} {'Nombre':<10} {'Email':<25} {'Fecha de nacimiento':<15}")
    print("-" * 65)
    for usuario in matriz:
        id_usuario = usuario[0]
        nombre = usuario[1]
        correo = usuario[2]
        fecha_nac = usuario[3]
        print(f"{id_usuario:<5} {nombre:<10} {correo:<25} {fecha_nac:>12}")

def eliminar_usuario(matriz_usuarios, user_id):
    for i, usuario in enumerate(matriz_usuarios):
        if usuario[0] == user_id:
            del matriz_usuarios[i]
            print(f"Usuario con ID: {user_id} eliminado.")
            return
    print(f"Usuario con ID: {user_id} no encontrado.")

imprimir_matriz_usuarios(matriz_usuarios)

