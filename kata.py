J = 11
Q = 12
K = 13

contador_repartir = 0
contador_jugadores = 0
contador_cartas = 0
cartas = [
    "3D", "JS", "7S", "KC", "JH", "6H", "JD", "5D", "5H", "10H", "8D", "4S", "2D",
    "5S", "9H", "JC", "6S", "QH", "4C", "QC", "4H", "1D", "7D", "KD", "8C", "10C",
    "6C", "1C", "QD", "QS", "2H", "3S", "9S", "1S", "3C", "8H", "1H", "KH", "2S",
    "9C", "KS", "10S", "8S", "4D", "5C", "7C", "3H", "9D", "2C", "6D", "7H", "10D"
]

jugadores = [[],[],[],[]]

while contador_repartir < 13:
    contador_jugadores = 0
    while contador_jugadores < 4:
        jugadores[contador_jugadores].append(cartas.pop())
        contador_jugadores += 1
    contador_repartir += 1


contador_jugadores = 0

lista_mano = []
while len(lista_mano) < 4:
    lista_mano.append(jugadores[contador_jugadores][contador_jugadores])
    contador_jugadores += 1

print(lista_mano)

contador_mano = 0

while contador_mano < 3:
    if 'D' in lista_mano[contador_mano]:
        contador_mano += 1
        while contador_mano < 3:
            if 'D' not in lista_mano[contador_mano]:
                contador_mano += 1
            print("Gana el jugador con la carta D")
            if 'D' in lista_mano[contador_mano]:
                contador_mano += 1