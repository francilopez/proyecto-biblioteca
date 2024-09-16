
import re 
from validacion import validar_email

def imprimir_matriz_usuarios(matriz):
"""
Pre: matriz es una lista de listas con cuatro elementos, donde los elementos representan el ID del usuario, nombre, correo electrónico, y fecha de nacimiento, respectivamente.
Pos: La función imprime una tabla con los detalles de los usuarios, con encabezados alineados y una línea de separación antes y después de los datos.
"""
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
"""
Pre: matriz_usuarios es una lista de listas con elementos como: ID, nombre, email y fecha de nacimiento. La función validar_email esta definida e implementada.
Pos: Si el ID del usuario ya existe o el email es inválido, se imprime un mensaje de error y no se añade el nuevo usuario. Si todo es válido, el nuevo usuario es agregado a matriz_usuarios.
"""
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
    """
Pre: matriz_usuarios es una lista de listas, donde el primer elemento es el ID del usuario. user_id es comparable con el primer elemento de los subelementos en matriz_usuarios.
Pos: Si se encuentra un usuario con el user_id especificado, ese usuario se elimina de matriz_usuarios y se imprime un mensaje de confirmación. Si el ID no se encuentra, se imprime un mensaje de que el usuario no fue encontrado.
    """
    for i, usuario in enumerate(matriz_usuarios):
        if usuario[0] == user_id:
            del matriz_usuarios[i]
            print(f"Usuario con ID: {user_id} eliminado.")
            return
    print(f"Usuario con ID: {user_id} no encontrado.")

def editar_usuario(matriz_usuarios):
    """
Pre: matriz_usuarios lista de listas. La entrada id_usuario debe ser un valor que puede ser convertido a un entero.
Pos: Si el id_usuario se encuentra en matriz_usuarios, los datos del usuario se actualizan y se imprime un mensaje de éxito. Si el ID no se encuentra, se imprime un mensaje de error. Si el ID no es un número entero, se imprime un mensaje indicando que el ID es inválido.
    """
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
        


        

