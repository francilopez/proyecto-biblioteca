from __main__ import *
from gestion_libros import *
from gestion_usuarios import *
from gestion_prestamos import *


archivo_prueba = 'usuarios_test.txt'

def test_leer_desde_txt():
    matriz_usuarios = leer_desde_txt(archivo_prueba)
    assert len(matriz_usuarios) == 2
    assert matriz_usuarios[0] == [1, "Juan", "juan@ejemplo.com", "01/01/2000"]

# Prueba para guardar en archivo txt
def test_guardar_en_txt():
    matriz_usuarios = [
        [1, "Juan", "juan@ejemplo.com", "01/01/2000"],
        [2, "Ana", "ana@ejemplo.com", "02/02/2001"]
    ]
    guardar_en_txt(matriz_usuarios, archivo_prueba)
    
    with open(archivo_prueba, 'r') as f:
        contenido = f.read()
    assert "1,Juan,juan@ejemplo.com,01/01/2000\n" in contenido
    assert "2,Ana,ana@ejemplo.com,02/02/2001\n" in contenido


# Prueba para eliminar un usuario
def test_eliminar_usuario():
    matriz_usuarios = leer_desde_txt(archivo_prueba)
    eliminar_usuario(matriz_usuarios, 1)
    assert len(matriz_usuarios) == 1
    assert matriz_usuarios[0][0] == 2




### python -m pytest pruebas_unitarias.py

