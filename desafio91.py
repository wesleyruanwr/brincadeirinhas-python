from random import randint
from time import sleep
from operator import itemgetter
sorteio = {'jogador 1' : randint(1, 6), 'jogador 2': randint(1, 6), 'jogador 3' : randint(1, 6), 'jogador 4': randint(1, 6)}
print('Sorteando...')
sleep(1)
for k, v in sorteio.items():
    print(f'{k} tirou {v}')
    sleep(1)
ranking = []
ranking = sorted(sorteio.items(), key = itemgetter(1), reverse= True)
print('--RANKING DOS JOGADORES--')
for i, v in enumerate(ranking):
    print(f'{i+1} lugar = {v[0]} com {v[1]}')