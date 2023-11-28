llista_tuples = []
lista_temporal = []
opcion = 1
posicion = 0
booleano = False

while opcion != 0:
    opcion = int(input("""
    ELige la opcion que deseas:
    0. Salir
    1. Afegir
    2. Eliminar
    3. Llistar
    OPCION:  """))

    if opcion == 1:
        nom_server = input("Introduce el nombre del servidor. ")
        IP = input("Introduce la direccion IPv4 del servidor. ")
        estado = input("Introduce el estado del servidor. ")
        tupla_server = (nom_server, IP, estado)
        llista_tuples.append(tupla_server)

    if opcion == 2:
        nombres_introducidos = input("Introduce el nombre del servidor que deseas eliminar de la lista. ")
        for posicion in range(0, len(llista_tuples)):
            if nombres_introducidos == llista_tuples[posicion][0]:
                llista_tuples.pop(posicion)
                booleano = True
            else:
                booleano = False
        
        if booleano == False:
            print("")
            print('El nombre de servidor que has introducido no existe')
                       
    if opcion == 3:
        print(llista_tuples)

print("Asi ha quedado tu lista:", llista_tuples)