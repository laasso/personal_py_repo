'''
    Crea un diccionari buit per emmagatzemar els dispositius, on les claus són els noms dels dispositius
    i els valors són les adreces IP.
    Permet a l'usuari afegir un dispositiu al diccionari.
    Permet a l'usuari eliminar un dispositiu del diccionari.
    Mostra tots els dispositius registrats al diccionari.
'''

#PRE: Pedir al usuario que escoja una opcion del 0 al 3
opcion = 1
diccionari_dispositius = {}
while opcion != 0:
    opcion = int(input("""
    ELige la opcion que deseas hacer con la lista:
    0. Salir
    1. Afegir
    2. Eliminar
    3. Llistar
    OPCION:  """))
  
    if opcion == 1:
        dispositiu = input('Introduce el dispositivo que quieras añadir al diccionario ')
        IP = input('Introduce la IP que quieras relacionar con el dispostivo ')
        diccionari_dispositius[dispositiu] = IP     

    elif opcion == 2:
        dispositiu = input('Introduce el dispositivo que quieras eliminar del diccionario ')
        if dispositiu not in diccionari_dispositius:
            print("El nombre que has introducido no existe en la lista")
        else:
            del diccionari_dispositius[dispositiu] 

    elif opcion == 3:
        print(diccionari_dispositius)
    

print("Asi ha quedado tu diccionario: ", diccionari_dispositius)

#POST: Devolver la opcion elegida
