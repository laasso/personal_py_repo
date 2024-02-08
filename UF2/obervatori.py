temp = []
day_counter = 0

exe_option = True
exe_option_input = ''

def RT(tlist,counter):
    aux_list = []
    aux_list = input()
    counter = counter + 7
    print(aux_list)
    aux_list = aux_list.split(' ')
    float_list = []
    for num in aux_list:
        float_list.append(float(num))

    print(float_list)


#hacer split para separar en diferentes posicions los datos y usar un float() para convertirlos
    
def dias(contador): 
    print(contador)

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
        RT(temp,day_counter)
