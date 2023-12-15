'''
 (Nom, Cognom, Edat, Nota1, Nota2, Nota3).
'''
#//PRE Usuario introduce datos

suma_media_op2 = []

pornota1 = int(30)
pornota2 = int(40)
pornota3 = int(30)

media_min_op2 = int(7)

alumnos_op_2 = []


#la lista alumnos_info es provisonal es para no tener que poner todo el rato los datos XD
alumnos_info = [["nicolas","rubiales", 18, 10, 10, 10],["iker", "macias", 19, 10, 10, 10],["carlos", "bonilla", 18, 10, 10, 9],["izan", "lozano",18, 8, 7, 5]]
'''
print(alumnos_info)
opcion_usuario = int(input('Introduce que deseas hacer '))

'''

for alumno in range(0,len(alumnos_info)):
    for info in range(3,len(alumnos_info)):
        suma_media_op2.append(alumnos_info[alumno][info] * pornota1 / 100)
        suma_media_op2.append(alumnos_info[alumno][info] * pornota2 / 100)
        suma_media_op2.append(alumnos_info[alumno][info] * pornota3 / 100)
        suma_media_op2 = sum(suma_media_op2)
        if suma_media_op2 > media_min_op2:
            alumnos_op_2.append(alumnos_info[alumno][0])
            suma_media_op2 = []
        suma_media_op2 = []

print(alumnos_op_2,"hola")
