#//PRE: Rep un nombre enter
numero_introduit = int(input("Introdueix un numero: "))
contador = 0
if numero_introduit > 1:
    for i in range(1, numero_introduit):
        if numero_introduit % i == 0:
            contador = contador + 1
    if contador == 1:
        print("Es primo")
    else:
        print("No es primo")
else:
    print("Introdueix un numero valid")
#POST// Mostra si es primo o no