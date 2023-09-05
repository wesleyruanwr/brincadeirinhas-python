from random import randint
from time import sleep
lista = []
jogo = []
tot = 1
quant = int(input('Quantos jogos você quer? '))
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogo.append(lista[:])
    lista.clear()
    tot += 1
print('-=' *3, f'Sorteando {quant} jogos','-=' *3)
for i, l in enumerate(jogo):
    print(f'Jogo {i+1}: {l}')
    sleep(1)