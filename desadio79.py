n = []
while True:
    num = (int(input('Adicione um número na lista: ')))
    if num not in n:
        n.append(num)
    opc = (str(input('Deseja adicionar mais um número? [S/N]: ')))[0]
    while opc not in 'NnSs':
        opc = (str(input('Deseja adicionar mais um número? [S/N]: ')))[0]
    if opc in 'Nn':
        break
n.sort()
print(f'Você digitou os números {n}')