CARES_DAU:int = 6

llista_tirades:list[int] = [0] * (CARES_DAU * 2 - 1)

def generar_histograma() -> None:
    generar_tirades()
    mostrar_histograma()
    mostrar_maximo()

def generar_tirades() -> None:
    dau1:int = 1
    
    while dau1 <= CARES_DAU:
        dau2:int = 1
        while dau2 <= CARES_DAU:
            llista_tirades[dau1 + dau2 - 2] += 1
            dau2 = dau2 + 1
        dau1 = dau1 + 1

def mostrar_histograma() -> None:
    for i in range(len(llista_tirades)):
        valor_tirada = calcular_valor_tirada(i)
        print(f"{valor_tirada}:", "*" * llista_tirades[i])    

def calcular_valor_tirada(i:int) -> str:
    valor = i + 2 
    if valor < 10:
        valor_tirada = f" {valor}"
    else:
        valor_tirada = f"{valor}"
        
    return valor_tirada

def mostrar_maximo() -> None:
    valor_tirada = calcular_valor_tirada_mes_repeticions()
    print(f"El maxim es {valor_tirada}.")    

def calcular_valor_tirada_mes_repeticions() -> int:
    maxim:int = 0
    maxim_tirades_index:int = 0 

    for valor in range (len(llista_tirades)):
        if llista_tirades[valor] > maxim:
            maxim = llista_tirades[valor]
            maxim_tirades_index = valor
    
    return maxim_tirades_index + 2

generar_histograma()
