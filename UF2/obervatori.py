temp = [[2,[1,2,3,4,5,6,7]],[3,[7,6,5,4,3,2,1,]]]


exe_option = True
exe_option_input = ''

def RT(tlist):
    temps = input()
    aux_list = []
    aux_list.append(temps)
    print(aux_list)
#hacer strip para separar en diferentes posicions los datos y usar un float() para convertirlos
while exe_option == True:
    exe_option_input = (input('''Benvingut al registre de temperatures
-------------------------------------
[RT] Registrar temperatures setmanals. 
[MJ] Consultar temperatura mitjana. 
[DF] Consultar diferència màxima. 
[FI] Sortir.
'''))
    if exe_option_input == 'FI':
        exe_option = False
    elif exe_option_input == 'RT':
        RT(temp)
