# PRE: Introduce un numero entero positivo
posicion = int(input("Introduce posicion de la serie Fibonacci: "))
valor1 = 1
valor2 = 1
contador = 0

while contador != posicion:
    if contador != posicion:
        valor1 = valor1 + valor2
        contador += 1
        print(valor1)
    if contador != posicion:
        valor2 = valor2 + valor1
        contador += 1
        print(valor2)

if valor1 > valor2:
    print(valor1)
else:
    print(valor2)

# POST: Devolver el numero de la serie fibonacci