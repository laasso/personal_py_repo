class Libro():
    def __init__(self, titulo, autor:str, ejemplares:int):
        self.titulo = titulo
        self.autor  = autor
        self.ejemplares = ejemplares

def prestar(self):
    if self.ejemplares > 0:
        self.ejemplares -= 1
        print(f'Llibre prestat: {self.titulo}, Autor: {self.autor}')
    else:
        print('No hay ejemplares')

def devolver(self):
    self.ejemplares += 1

def informacion(self):
    print(f'Llibre: {self.titulo}, Autor: {self.autor}, Ejemplares{self.ejemplares}')
