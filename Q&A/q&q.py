#//PRE: L'usuari respon les preguntes en minuscula

llista_preguntes = [
'Madrid es la capital de Espanya?', 'si']
['Estas cursando ASIX?', 'si']
['En que ciudad juega el Barsa?', 'barcelona']
['Este codigo esta escrito en C++?', 'no']
['El cielo es azul?', 'si'
]

score = 0


seed = 2
random = (seed * 503) % 1000 / 100
numero_pregunta = int(random * (len(llista_preguntes)))

resposta = str(input((llista_preguntes[numero_pregunta])))
print(resposta)