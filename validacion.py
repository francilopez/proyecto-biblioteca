                           #### VALIDACION #####
# Validación de fecha para los prestamos ACORREGIR O CAMBIAR
import datetime
import re

def validar_fecha(fecha_str):
    """ Valida que la fecha sea un formato correcto y no sea una fecha futura """
    try:
        fecha = datetime.datetime.strptime(fecha_str, '%Y-%m-%d').date()
        if fecha > datetime.date.today():
            raise ValueError("La fecha no puede ser futura.")
        return fecha
    except ValueError as e:
        print(f"Error de fecha: {e}")
        return None
    

def validar_email(email):
    patron = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, email) is not None