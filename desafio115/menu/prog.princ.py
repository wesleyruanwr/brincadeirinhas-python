from desafio115 import menu
while True:
    print('-' *30)
    print('MENU PRINCIPAL')
    print('-' *30)
    opc = ('1- Ver pessoas cadastradas\n'
        '2- cadastrar nova pessoa\n'
        '3- Sair do sistema')
    if opc == 3:
        break
    if opc == 1 or 2:
        menu.numenu(opc)