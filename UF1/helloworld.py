def calculadora():
    SUMA = 1
    RESTA= 2
    TXT_INTRODUCIR_NUMERO = ("Introduce un numero por pantalla")
    TXT_INTRODUCIR_OPERADOR = ("Introduce que operacion hacemos 1 para suma 2 para resta")
    a = int(input(TXT_INTRODUCIR_NUMERO))
    operador = int(input(TXT_INTRODUCIR_OPERADOR))
    b = int(input(TXT_INTRODUCIR_NUMERO))

    if operador == 1:
        result = a + b
    else:
        if operador == 2:
            result = a - b
        else:
           result = "Operacion no esta permitida"
    print(result)

calculadora()
