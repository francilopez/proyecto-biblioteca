                           #### VALIDACION #####
import datetime
import re

def validar_fecha(fecha_str):
    """
    Args:
        fecha_str: Fecha a validar en formato 'AAAA-MM-DD'.
    Returns:
        Tupla con (año, mes, día) si la validación es exitosa.
        None: Si la validación falla.
    """
    try:
        # Convertir la cadena a un objeto
        fecha = datetime.datetime.strptime(fecha_str, '%Y-%m-%d').date()  
        # Verificar que la fecha no sea futura
        if fecha > datetime.date.today():
            print("La fecha no puede ser en el futuro.")
            return None
        # Descomponer la fecha en año, mes y día
        fecha_tuple = (fecha.year, fecha.month, fecha.day)
        return fecha_tuple
    except ValueError:
        print("Fecha inválida. Utilizar AAAA-MM-DD")
        return None

def validar_email(email):
    patron = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, email) is not None
