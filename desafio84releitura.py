dados = []
pessoas = []
pesmai = pesmen = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        pesmai = pesmen = dados[1]
    else:
        if dados[1] > pesmai:
            pesmai = dados[1]
        if dados[1] < pesmen:
            pesmen = dados[1]
    pessoas.append(dados)
    dados.clear()
    while True:
        opc = str(input('Deseja continuar?[S/N]: ')).strip().upper()[0]
        if opc in 'SN':
            break
    if opc == 'N':
        break
print(f'Ao todo, foram cadastradas {len(pessoas)} pessoas')
print(f'O maior peso foi de {pesmai}Kg . Peso de ', end='')
for p in pessoas:
    if p[1] == pesmai:
        print(f'[{p[0]}]')  
print(f'O menor peso foi de {pesmen}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == pesmen:
        print(f'[{p[0]}]')

#No do professor eu consigo mostrar o nome das pessoas que tiverem o msm peso maior ou menor
#ja no meu eu consigo mostrar os 2 pesos maiores e menores mas sem o nome
