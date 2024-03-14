'''
Descompon aquest codi en funcions més petites per millorar la seva modularitat i reutilització. 

Pista: Volem poder moure'ns per una graella bidimensional.

Codi Python:
'''
class bidimensional():
    # Programa principal
    def __init__(self):
        self.coordenada = (0, 0)

    def moure_dreta(self, coordenada):
        x, y = coordenada
        nova_coordenada = (x + 1, y)
        return nova_coordenada

    def moure_esquerra(self, coordenada):
        x, y = coordenada
        nova_coordenada = (x - 1, y)
        return nova_coordenada

    def moure_amunt(self, coordenada):
        x, y = coordenada
        nova_coordenada = (x, y + 1)
        return nova_coordenada

    def moure_avall(self, coordenada):
        x, y = coordenada
        nova_coordenada = (x, y - 1)
        return nova_coordenada
    
# Coordenada inicial
bi = bidimensional()
# Executar moviments
coordenada = bi.moure_dreta(bi.coordenada)
print(f"Nova coordenada després de moure a la dreta: {coordenada}")

coordenada = bi.moure_amunt(bi.coordenada)
print(f"Nova coordenada després de moure amunt: {coordenada}")