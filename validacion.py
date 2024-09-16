                           #### VALIDACION #####
# Validación de fecha para los prestamos ACORREGIR O CAMBIAR
import datetime
import re

def validar_fecha(fecha_str):
    """ 
Pre: fecha_str debe ser una cadena de caracteres en el formato 'YYYY-MM-DD'. El módulo datetime tiene que estar importado.
Pos: La función valida que la fecha esté en el formato correcto y que no sea una fecha futura. Si la validación es exitosa, retorna el objeto date correspondiente a la fecha. Si la fecha es incorrecta, imprime un mensaje de error.  
    """
    try:
        fecha = datetime.datetime.strptime(fecha_str, '%Y-%m-%d').date()
        if fecha > datetime.date.today():
            raise ValueError("La fecha no puede ser futura.")
        return fecha
    except ValueError as e:
        print(f"Error de fecha: {e}")
        return None
    

def validar_email(email):
  """
Pre: email tiene que ser una cadena de caracteres. El módulo re tiene que estar importado.
Pos: La función valida si la cadena email tiene el formato de una dirección de correo electrónico. Retorna True si el formato es correcto según el patrón de la expresión regular, y False si no lo es.
  """
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, email) is not None
