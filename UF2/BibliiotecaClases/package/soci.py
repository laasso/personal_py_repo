class Soci():
    def __init__(self, nombre:str,apellido:str, numero_socio:int ):
        self.nombre = nombre
        self.apellido = apellido
        self.numero_socio = numero_socio

    def solicitar_pretamo(self, libro: Libro, fecha_prestamo: str):
        print(f'Prestamo solicitado por" {self.nombre}')
    prestamo: Prestamo = Prestamo(libro, self)
    prestamo.registrarPrestamo(fecha_prestamo)

    def devolver_prestamo(self, libro: Libro):
        prestamo: Prestamo = Prestamo(libro,self)
        prestamo.devolverPrestamo()

    def informacion(self):
        ...