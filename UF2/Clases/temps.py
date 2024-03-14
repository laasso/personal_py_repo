class Temperatura:

    def __init__(self, valor:int) -> None:
        self.valor = 0
        self.unidad =  'Celsius0'

    def escribir (self) -> None:
        print(self.valor, self.unidad)

    def pasar_a_far (self) -> None:
        self.valor = (self.valor * 9/5) + 32
        self.unidad = 'Fahrenheit'

    def pasar_a_celsius (self) -> None:
        self.valor = (self.valor - 32) * 5/9
        self.unidad = 'Celsisu'


ayer = Temperatura(14)


hoy = Temperatura(8)

ayer.escribir()

hoy.pasar_a_far()
ayer.escribir()
hoy.escribir()

hoy.escribir()

