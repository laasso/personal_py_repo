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

