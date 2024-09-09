                           #### VALIDACION #####
# Validación de fecha para los prestamos ACORREGIR O CAMBIAR
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