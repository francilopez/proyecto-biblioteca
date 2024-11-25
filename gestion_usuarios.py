import re 
from validacion import validar_email

def leer_desde_txt(archivo):
    # pre: parámetro archivo representa al archivo de texto que contiene los datos a leer. El archivo debe existir y tener datos en formato CSV.
    # pos: lee el archivo especificado y carga sus datos en una matriz (matriz_usuarios), donde cada lista representa una línea del archivo
    matriz_usuarios = []
    try:
        with open(archivo, 'r') as f:
            for linea in f:
                datos = linea.strip().split(',')
                datos[0] = int(datos[0])
                matriz_usuarios.append(datos)
        print(f"Matriz cargada desde {archivo} exitosamente.")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
    
    return matriz_usuarios





def guardar_en_txt(matriz_usuarios, archivo):
    # pre:  parámetro matriz_usuarios es una matriz, donde cada lista representa un usuario con al menos cuatro elementos. archivo es ruta y nombre del archivo donde se guardarán los datos.
    # pos: guarda los datos de los usuarios en el archivo especificado por archivo, con cada usuario representado como una línea en formato CSV 
    try:
        with open(archivo, 'w') as f:
            for usuario in matriz_usuarios:
                linea = f"{usuario[0]},{usuario[1]},{usuario[2]},{usuario[3]}\n"
                f.write(linea)
    except Exception as e:
        print(f"Error al guardar en el archivo: {e}")





def imprimir_matriz_usuarios(matriz):
    # pre: parámetro matriz sea una matriz, donde cada lista representa un usuario con al menos cuatro elementos
    # pos: imprime en formato tabular los datos de cada usuario en la matriz. La tabla incluye las columnas "ID", "Nombre", "Email" y "Fecha de nacimiento".
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
    # pre: parámetro matriz_usuarios sea una matriz, donde cada lista representa un usuario y contiene al menos cuatro elementos: ID, nombre, correo electrónico y fecha de nacimiento.
    # pos: asigna un nuevo ID al usuario, solicita al usuario que ingrese el nombre, correo electrónico y fecha de nacimiento del nuevo usuario, valida el formato del correo electrónico, y si es válido, agrega los datos del nuevo usuario a la lista matriz_usuarios como una nueva sublista. 

    id_usuario = matriz_usuarios[-1][0] + 1 
    nombre = input("Ingrese el nombre del nuevo usuario: ")
    email = input("Ingrese el Email del nuevo usuario: ")
    
    if not validar_email(email):
        print("Error: El formato del email no es válido.")
        return

    fecha_nacimiento = input("Ingrese la fecha de nacimiento del nuevo usuario (DD/MM/AAAA): ")
    nuevo_usuario = [id_usuario, nombre, email, fecha_nacimiento]
    matriz_usuarios.append(nuevo_usuario)






def eliminar_usuario(matriz_usuarios, user_id):
    # pre: parámetro matriz_usuarios sea una matriz, donde cada lista representa un usuario con al menos el primer elemento como su ID único. user_id debe representar el ID del usuario que se desea eliminar.
    # pos:  busca un usuario en matriz_usuarios cuyo primer elemento (ID) coincida con user_id. Si encuentra el usuario, lo elimina de la lista.
    for i, usuario in enumerate(matriz_usuarios):
        if usuario[0] == user_id:
            del matriz_usuarios[i]
            print(f"Usuario con ID: {user_id} eliminado.")
            return
    print(f"Usuario con ID: {user_id} no encontrado.")






def editar_usuario(matriz_usuarios):
    # pre: parámetro matriz_usuarios sea una matriz, donde cada lista representa un usuario y contiene al menos cuatro elementos: ID del usuario, nombre, correo electrónico y fecha de nacimiento.
    # pos: solicita al usuario el id_usuario del usuario que desea editar. Si encuentra un usuario con ese ID, permite ingresar un nuevo nombre, correo electrónico y fecha de nacimiento para actualizar los datos del usuario en la lista.
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
        




        

