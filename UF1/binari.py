'''
    Demana a l'usuari que introdueixi un número binari (una cadena de 0s i 1s).
    Converteix el número binari al seu equivalent decimal.
    Mostra el resultat de la conversió.
'''

#PRE: Recibimos un numero binario introducido por el usuario

binari = []
auxiliar = []
final_binario = False
size_variable = 1
i = 0
decimal = 0

binari = list(input("Introduce un codigo binario que quieras pasar a decimal: "))

while not final_binario:
    auxiliar = [None] * (size_variable)

    for j in range(0, size_variable):
        auxiliar[j] = binari[j]

    if auxiliar == binari:
        final_binario = True
    
    decimal = (int(decimal) * 2) + int(binari[i])

    final_binario = auxiliar == binari
    size_variable += 1
    i += 1

print(decimal)

#POST: Mostrar el numero decimal al usuario transformado de binario