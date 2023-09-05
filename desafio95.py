jogador = {}
geral = []
gols = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    gols.clear()
    for c in range(0, jogador['partidas']):
        gols.append(int(input(f'Quantos gols na {c+1} partida? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    geral.append(jogador.copy())
    opc = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while opc not in 'SN':
        print('ERRO responda apenas S ou N')
        opc = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opc == 'N':
        break
print('-=' *30)
print('cod', end='  ')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-='* 30)
for k, v in enumerate(geral):
    print(f'{k:<4}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    opc = int(input('Digite o código do jogador que deseja detalhar (999 PARA PARAR): '))
    if opc == 999:
        print('Finalizando programa...')
        break
    if opc > len(geral):
        print('Erro, código inexistente')
    else:
        print('-=' *30)
        print(f'Detalhes do jogador {geral [opc]["nome"]}:')
        for i, y in enumerate(geral [opc] ["gols"]):
            print('-' *30)
            print(f'No jogo {i+1} fez {y} gols')
