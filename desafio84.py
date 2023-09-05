pessoas = []
dados = []
quant = 0
cont = 0
while True:
    nome = str(input('nome: '))
    dados.append(nome)
    peso = int(input('peso: '))
    dados.append(peso)
    if cont == 0:
        pesmai = pesmen = pesmai1 = pesmen1 = peso
    else:
        if pesmai < peso:
            pesmai1 = pesmai
            pesmai = peso
        if pesmen > peso:
            pesmen1 = pesmen
            pesmen = peso
    pessoas.append(dados[:])
    quant += 1
    cont += 1
    dados.clear
    while True:
        opc = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if opc in 'SN':
            break
    if opc == 'N':
        break
print(f'Ao todo foram cadastradas {quant} pessoas')
print(f'Os maiores pesos foram {pesmai} e {pesmai1}')
print(f'Os menores pesos foram {pesmen} e {pesmen1}')
