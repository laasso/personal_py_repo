CARES_DAU:int = 6

llista_tirades:list[int] = [0] * (CARES_DAU * 2 - 1)

def generar_histograma() -> None:
    generar_tirades()

def generar_tirades() -> None:
    dau1:int = 1
    
    while dau1 <= CARES_DAU:
        dau2:int = 1
        while dau2 <= CARES_DAU:
            llista_tirades[dau1 + dau2 - 2] += 1
            dau2 = dau2 + 1
        dau1 = dau1 + 1

def calcular_valor_tirada(i:int) -> str:
    valor = i + 2 
    if valor < 10:
        valor_tirada = f" {valor}"
    else:
        valor_tirada = f"{valor}"
        
    return valor_tirada

generar_histograma()
print(llista_tirades)