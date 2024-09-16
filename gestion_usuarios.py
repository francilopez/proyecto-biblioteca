
import re 
from validacion import validar_email

def imprimir_matriz_usuarios(matriz):

    print(f"{'ID':<5} {'Nombre':<10} {'Email':<25} {'Fecha de nacimiento':<15}")
    print("-" * 65)
    for usuario in matriz:
        id_usuario = usuario[0]
        nombre = usuario[1]
        correo = usuario[2]
        fecha_nac = usuario[3]
        print(f"{id_usuario:<5} {nombre:<10} {correo:<25} {fecha_nac:>12}")
    print("-" * 65)

def agregar_usuario(matriz_usuarios):

    id_usuario = int(input("Ingrese el ID del nuevo usuario: "))

    if any(usuario[0] == id_usuario for usuario in matriz_usuarios):
        print("Error: El ID ya está en uso. No se puede agregar el usuario.")
        return
    
    nombre = input("Ingrese el nombre del nuevo usuario: ")
    email = input("Ingrese el Email del nuevo usuario: ")
    
    if not validar_email(email):
        print("Error: El formato del email no es válido.")
        return

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

def editar_usuario(matriz_usuarios):
    try:
        id_usuario = int(input("ingrese el ID del usuario: "))
        for usuario in matriz_usuarios:
            if usuario[0] == id_usuario:
                nuevo_nombre = input(f"Ingrese el nuevo nombre para el usuario (actual: {usuario[1]}): ")
                nuevo_email = input(f"Ingrese el nuevo email para el usuario (actual: {usuario[2]}): ")
                nueva_fecha_nacimiento = input(f"Ingrese la nueva fecha de nacimiento para el usuario (actual: {usuario[3]}): ")

                usuario[1] = nuevo_nombre
                usuario[2] = nuevo_email
                usuario[3] = nueva_fecha_nacimiento

                print("Datos del usuario actualizados exitosamente.")
                return
        print(f"Usuario con ID: {id_usuario} no encontrado.")
    except ValueError:
        print("ID inválido. Debe ser un número entero.")
        


        

