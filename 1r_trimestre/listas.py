'''
    Creeu una llista buida per emmagatzemar els noms d'usuari.
    Permet a lusuari afegir un nom a la llista.
    Permet a lusuari eliminar un nom de la llista.
    Mostra tots els noms d'usuari emmagatzemats.
'''

#PRE: Pedir al usuario que escoja una opcion del 0 al 3

llista_noms = []
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
        nom = input("Introduce un nombre que quieras añadir a la lista. ")
        llista_noms.append(nom)

    elif opcion == 2:
        nom = input("Introduce un nombre que quieras eliminar de la lista. ")
        if nom not in llista_noms:
            print("El nombre que has introducido no existe en la lista")
        else:
            llista_noms.remove(nom)

    elif opcion == 3:
        print(llista_noms)

print("Asi ha quedado tu lista:", llista_noms)

#POST: Devolver la opcion elegida