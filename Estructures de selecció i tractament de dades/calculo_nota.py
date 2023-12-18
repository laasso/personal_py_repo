'''
 (Nom, Cognom, Edat, Nota1, Nota2, Nota3).
'''
#//PRE Usuario introduce datos

suma_media_op2 = []

checker = False

pornota1 = int(30)
pornota2 = int(40)
pornota3 = int(30)

media_min_op2 = int(7)

alumnos_op_2 = []
alumnos_op_3 = []

nota1 = 0
#la lista alumnos_info es provisonal es para no tener que poner todo el rato los datos XD
alumnos_info = [["nicolas","rubiales", 18, 1, 9, 7],["iker", "macias", 19, 7, 10, 10],["carlos", "bonilla", 18, 10, 10, 9],["izan", "lozano",18, 8, 8, 5]]
'''
print(alumnos_info)
opcion_usuario = int(input('Introduce que deseas hacer '))

'''

for alumno in range(0,len(alumnos_info)):
    for info in range(3,len(alumnos_info[alumno])):
        suma_media_op2.append(alumnos_info[alumno][info] * pornota1 / 100)
        suma_media_op2.append(alumnos_info[alumno][info] * pornota2 / 100)
        suma_media_op2.append(alumnos_info[alumno][info] * pornota3 / 100)
        suma_total_media_op2 = sum(suma_media_op2)
        if suma_total_media_op2 > media_min_op2 & checker == False:
            alumnos_op_2.append(alumnos_info[alumno][0])
            checker = True
        suma_media_op2 = []
    checker = False
    
checker = False
alumnos_op_2 = tuple(alumnos_op_2)
print(alumnos_op_2,"hola")




for alumno in range(0,len(alumnos_info)):
    for nota in range(3,len(alumnos_info[alumno])):
        if alumnos_info[alumno][nota] > 8 & checker == False:
            alumnos_op_3.append(alumnos_info[alumno][0])
            checker = True
    checker = False
alumnos_op_3 = tuple(alumnos_op_3)
print(alumnos_op_3)

