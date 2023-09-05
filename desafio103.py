def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gols')


nome = str(input('Nome do jogador: '))
gols = str(input('Quantidade de gols: '))       #leio o numero como string
if gols.isnumeric():                            #uso o "isnumeric()" para verificar se e um numero
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':                          #se o input de "nome" sem espacos, vier vazio
    ficha(gols=gols)                            #a def sera apenas com os gols
else:
    ficha(nome, gols)                           #se nao, a def usa os dois parametros