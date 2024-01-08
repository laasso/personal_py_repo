#//PRE: L'usuari respon les preguntes en minuscula

llista_preguntes = [
['Madrid es la capital de Espanya?', 'si'],
['Estas cursando ASIX?', 'si'],
['En que ciudad juega el Barsa?', 'barcelona'],
['Este codigo esta escrito en C++?', 'no'],
['El cielo es azul?', 'si']
]

score = 0
opcio = 1
seed = 2

print("""
Benvingut al joc de preguntes i respostes
Cada resposta correcta et suma un punt
    """)

while opcio != 0:
    opcio = int(input("""
Selecciona una opcio:
    0. Sortir
    1. Respondre
    """))
    if opcio == 1:
        seed = (seed * 997) % 1000
        random = (seed * 503) % 1000 / 1000
        numero_pregunta = int(random * (len(llista_preguntes)))
        print(numero_pregunta)
        print(seed)
        resposta = str(input((llista_preguntes[numero_pregunta][0])))
        if resposta == llista_preguntes[numero_pregunta][1]:
            print("Resposta correcta!")
            score = score + 1
            print("La teva puntuacio:",score)
        else:
            print("Resposta incorrecta")
            print("La teva puntuacio:",score)
print("La teva puntuacio final es:",score)



