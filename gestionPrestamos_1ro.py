### PRIMERA APROXIMACIÓN DEL CODIGO PARA GESTION DE PRESTAMOS
##Gestión de Préstamos 
# o Registrar préstamos de libros a los clientes.
# o Leer y visualizar el historial de préstamos. 
# o Actualizar la información de los préstamos (fechas, estado). 
# o Registrar la devolución de libros y actualizar el estado del préstamo. 

def registrar_prestamo(self, usuario_id, titulo_libro):
        """ Registra un préstamo de libro a un usuario. """
        libro = self.buscar_libro(titulo_libro)
        if usuario_id not in self.usuarios:
            raise ValueError("Usuario no registrado")
        if libro['estado'] == 'prestado':
            raise ValueError("Libro ya prestado")

        fecha_prestamo = datetime.date.today()
        fecha_devolucion = fecha_prestamo + datetime.timedelta(days=14)  # 2 semanas para devolver
        libro['estado'] = 'prestado'
        self.prestamos[usuario_id] = {'titulo': titulo_libro, 'fecha_prestamo': fecha_prestamo, 'fecha_devolucion': fecha_devolucion}
        self.usuarios[usuario_id]['prestamos'].append(self.prestamos[usuario_id])

def leer_historial_prestamos(self, usuario_id):
            """ Lee y visualiza el historial de préstamos de un usuario. """
            if usuario_id not in self.usuarios:
                raise ValueError("Usuario no registrado")
            return self.usuarios[usuario_id]['prestamos']

def actualizar_prestamo(self, usuario_id, nuevo_estado):
    """ Actualiza la información de un préstamo. """
    if usuario_id not in self.prestamos:
        raise ValueError("No hay préstamos registrados para este usuario")

    libro_prestado = self.prestamos[usuario_id]
    libro = self.buscar_libro(libro_prestado['titulo'])
        
    if nuevo_estado == 'devuelto':
        libro['estado'] = 'disponible'
        self.prestamos.pop(usuario_id)
    else:
        raise ValueError("Estado no válido")

def registrar_devolucion(self, usuario_id):
    """ Registra la devolución de un libro y actualiza el estado del préstamo. """
    self.actualizar_prestamo(usuario_id, 'devuelto')
