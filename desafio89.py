dados = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('1ª nota: '))
    nota2 = float(input('2ª nota: '))
    media = (nota1 + nota2) / 2
    dados.append([nome, [nota1, nota2], media])
    opc = str(input('Deseja continuar?[S/N]: ')).strip().upper()[0]
    while opc not in 'SN':
        opc = str(input('Deseja continuar?[S/N]: ')).strip().upper()[0]
    if opc == 'N':
        break
print('-=' * 20)
print(f'{"No":<4}{"nome":<10}{"media":>12}')
print('-=' * 20)
for i, a in enumerate(dados):
    print(f'{i:<4} {a[0]:<10} {a[2]:>8}')
while True:
    esc = int(input('Deseja ver as notas de qual aluno? (999 para parar) '))
    for i, a in enumerate(dados):
        if esc == i:
            print(f'Aluno: {a[0]}')
            print(f'notas: {a[1]}')
    if esc == 999:
        break
print('FIM DO PROGRAMA')
