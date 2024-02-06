temp = [[2,[1,2,3,4,5,6,7]],[3,[7,6,5,4,3,2,1,]]]


exe_option = True
exe_option_input = ''
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
        print('works')