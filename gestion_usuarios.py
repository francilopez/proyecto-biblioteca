


def imprimir_matriz_usuarios(matriz):

    print(f"{'ID':<5} {'Nombre':<10} {'Email':<25} {'Fecha de nacimiento':<15}")
    print("-" * 65)
    for usuario in matriz:
        id_usuario = usuario[0]
        nombre = usuario[1]
        correo = usuario[2]
        fecha_nac = usuario[3]
        print(f"{id_usuario:<5} {nombre:<10} {correo:<25} {fecha_nac:>12}")

def agregar_usuario(matriz_usuarios):
    
    id_usuario = int(input("Ingrese el ID del nuevo usuario: "))
    nombre = input("Ingrese el nombre del nuevo usuario: ")
    email = input("Ingrese el Email del nuevo usuario: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento del nuevo usuario (DD/MM/AAAA): ")


    nuevo_usuario = [id_usuario, nombre, email, fecha_nacimiento]
    
    matriz_usuarios.append(nuevo_usuario)

def eliminar_usuario(matriz_usuarios, user_id):
    for i, usuario in enumerate(matriz_usuarios):
        if usuario[0] == user_id:
            del matriz_usuarios[i]
            print(f"Usuario con ID: {user_id} eliminado.")
            return
    print(f"Usuario con ID: {user_id} no encontrado.")
