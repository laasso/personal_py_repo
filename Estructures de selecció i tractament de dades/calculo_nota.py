
#//PRE Usuario introduce datos que corresponden con el tipo de datos que se piden

suma_media_op2 = []

checker = False
checker2 = False

pornota1 = int(30)
pornota2 = int(40)
pornota3 = int(30)

media_min_op2 = int(7)

alumnos_op_2 = []
alumnos_op_3 = []

numero_notes = 3
numero_alumnes = int(input("Quants alumnes evaluarem:"))

alumnos_info = [None] * numero_alumnes

for i in range(numero_alumnes):
    name = input("Nom de l'alumne: ")
    surname = input("Cognom de l'alumne: ")
    age = int(input("Edat de l'alumne: "))
    notes = [None] * numero_notes
    for j in range(numero_notes):
        notes[j] = int(input(f"Nota {j} de l'alumne: "))
    alumnos_info[i] = (name, surname, age, notes[0], notes[1], notes[2])

for alumno in range(0,len(alumnos_info)):
    for info in range(3,len(alumnos_info[alumno])):
        suma_media_op2.append(alumnos_info[alumno][info] * pornota1 / 100)
        suma_media_op2.append(alumnos_info[alumno][info] * pornota2 / 100)
        suma_media_op2.append(alumnos_info[alumno][info] * pornota3 / 100)
        suma_total_media_op2 = sum(suma_media_op2)
        if suma_total_media_op2 > media_min_op2 & checker == False:
            alumnos_op_2.append(alumnos_info[alumno])
            checker = True
        suma_media_op2 = []
    checker = False

alumnos_op_2 = tuple(alumnos_op_2)




for alumno in range(0,len(alumnos_info)):
    for nota in range(3,len(alumnos_info[alumno])):
        if alumnos_info[alumno][nota] > 8 & checker2 == False:
            checker2 = True
    if checker2 == True:
        alumnos_op_3.append(alumnos_info[alumno])
    checker2 = False
alumnos_op_3 = tuple(alumnos_op_3)



print("Mitjana Superior a 7")
for alumne in alumnos_op_2:
    print("\tNom:", end=" ")
    print(alumne[0], end=" ")
    print("Cognom:", end=" ")
    print(alumne[1], end=" ")
    print("Edat:", end=" ")
    print(alumne[2], end=" ")
    print("Nota 1:", end=" ")
    print(alumne[3], end=" ")
    print("Nota 2:", end=" ")
    print(alumne[4], end=" ")
    print("Nota 3:", end=" ")
    print(alumne[5])

print("Alguna nota superior a 8")
for alumne in alumnos_op_3:
    print("\tNom:", end=" ")
    print(alumne[0], end=" ")
    print("Cognom:", end=" ")
    print(alumne[1], end=" ")
    print("Edat:", end=" ")
    print(alumne[2], end=" ")
    print("Nota 1:", end=" ")
    print(alumne[3], end=" ")
    print("Nota 2:", end=" ")
    print(alumne[4], end=" ")
    print("Nota 3:", end=" ")
    print(alumne[5]) 

#//POST Se muestran los nombres ordenados