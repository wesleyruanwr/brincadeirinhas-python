dados = []
princ = {}
totidade = 0
while True:
    princ.clear()
    princ['nome'] = str(input('nome: '))
    princ['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while princ['sexo'] not in 'MF':
        print('ERRO responda apenas M ou F')
        princ['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    princ['idade'] = int(input('idade: '))
    totidade += princ['idade']
    dados.append(princ.copy())
    opc = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while opc not in 'SN':
        print('ERRO responda apenas S ou N')
        opc = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opc == 'N':
        break
media = totidade / len(dados)
print(f'Ao todo foram {len(dados)} pessoas cadastradas ')
print(f'A media de idade e {media:5.2f}')
print(f'As mulheres cadastradas foram: ', end='')
for p in dados:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}')
print(f'A lista de pessoas que estao acima da media: ')
for p in dados:
    if p['idade'] >= media:
        print(f'{p["nome"]}; {p["idade"]}; {p["sexo"]}')
