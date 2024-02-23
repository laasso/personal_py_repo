CARES_DAU:int = 6

llista_tirades:list[int] = [0] * (CARES_DAU * 2 - 1)

numero_tirades = CARES_DAU * CARES_DAU


def generar_histograma() -> None:
    generar_tirades()
    mostrar_probabilitat()

def mostrar_probabilitat() -> None:
    probabilitat = calcular_probabilitat()
    print(f"La probabilitat es de {probabilitat}%")

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

def llegir_valor() -> int:
    valor_introduit:int = 0
    while valor_introduit == 0:
        valor_introduit = int(input("Escriu el valor a calcular [2 - 12]."))
        if valor_introduit < 2 or valor_introduit > 12:
            valor_introduit = 0
            print("El valor no es entre 2 i 12")
    return valor_introduit

def calcular_probabilitat() -> float:
    probabilitat:float = 0.0
    valor:int = llegir_valor()
    suma:int = 0
    for i in range(len(llista_tirades)):
        if i == valor:
            for j in range(0,valor - 1):
                suma = llista_tirades[j] + suma
            probabilitat = ((suma * 100)/numero_tirades)
    probabilitat = int(probabilitat)
    probabilitat = float(probabilitat)
    return probabilitat
            


generar_histograma()
