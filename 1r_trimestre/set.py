'''
    Crea un set buit per emmagatzemar els números de ports oberts.
    Permet a l'usuari afegir un port al set.
    Permet a l'usuari tancar un port al set.
    Mostra tots els ports oberts al set.
'''

#PRE: 

llista_ports = []
set_ports = set(llista_ports)

opcion = 1

while opcion != 0:
    opcion = int(input("""
    ELige la opcion que deseas hacer con la lista:
    0. Salir
    1. Afegir
    2. Eliminar
    3. Llistar
    OPCION:  """))

    if opcion == 1:
        port = int(input("Introduce un nombre que quieras añadir a la lista. "))
        set_ports = set(llista_ports)
        llista_ports.append(port)

    elif opcion == 2:
        port = int(input("Introduce un nombre que quieras eliminar de la lista. "))
        if port not in llista_ports:
            print("El nombre que has introducido no existe en la lista")
        else:
            set_ports = set(llista_ports)
            set_ports.discard(port)

    elif opcion == 3:
        print(set_ports)

print("Asi ha quedado tu lista:", set_ports)
