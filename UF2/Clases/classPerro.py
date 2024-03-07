class Perro:
    def __init__(self, nombre):
        self.nombre = nombre 
    
    def ladrar(self):
        print(f"{self.nombre}buf buf")

    def correr(self):
        print("Esta corriendo")

    def comer(self):
        print("Esta comiendo")

perro1 = Perro("Tobby")
perro2 = Perro()

perro1.ladrar()
perro2.comer()