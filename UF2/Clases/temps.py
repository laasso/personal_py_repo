class Temperatura:

    def __init__(self):
        self.valor = 0
        self.unidad =  'Celsius0'

    def escribir (self):
        print(self.valor, self.unidad)

    def pasar_a_far (self):
        self.valor = (self.valor * 9/5) + 32
        self.unidad = 'Fahrenheit'

    def pasar_a_celsius (self):
        self.valor = (self.valor - 32) * 5/9
        self.unidad = 'Celsisu'


ayer = Temperatura()
ayer.valor = 14

hoy = Temperatura()
hoy.valor = 8
ayer.escribir()

hoy.pasar_a_far()
ayer.escribir()
hoy.escribir()

hoy.escribir()

