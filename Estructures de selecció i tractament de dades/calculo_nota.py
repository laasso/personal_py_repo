'''
 (Nom, Cognom, Edat, Nota1, Nota2, Nota3).
'''
#//PRE Usuario introduce datos

suma_media_op2 = []

pornota1 = int(30)
pornota2 = int(40)
pornota3 = int(30)

media_min_op2 = int(7)




#la lista alumnos_info es provisonal es para no tener que poner todo el rato los datos XD
alumnos_info = [["nicolas","rubiales", 18, 10, 10, 10],["iker", "macias", 19, 5, 4, 10],["carlos", "bonilla", 18, 0, 10, 9],["izan", "lozano",18, 8, 7, 5]]
'''
print(alumnos_info)
opcion_usuario = int(input('Introduce que deseas hacer '))

'''

for alumno in alumnos_info:
    suma_media_op2.append(alumnos_info[1][3] * pornota1 / 100)
    suma_media_op2.append(alumnos_info[1][4] * pornota2 / 100)
    suma_media_op2.append(alumnos_info[1][5] * pornota3 / 100)
    print(sum(suma_media_op2))


