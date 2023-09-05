lista = []
listap = []
listai = []
while True:
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        listap.append(n)
        lista.append(n)
    elif n % 2 != 0: 
        lista.append(n)
        listai.append(n)
    opc = str(input('Quer digitar mais um número?[S/N]:' )).strip().upper()[0]
    while opc not in 'SN':
        opc = str(input('Quer digitar mais um número?[S/N]:' )).strip().upper[0]
    if opc == 'N':
        break
print(f'A lista completa foi: {lista}')
print(f'A lista com números pares foi: {listap}')
print(f'A lista com números ímpares foi: {listai}')
