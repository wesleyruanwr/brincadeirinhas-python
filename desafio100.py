from random import randint
lista=[]
def sorteia():
    c = 0
    while c <= 5:
        num = randint(0, 100)
        lista.append(num)
        c += 1
        if c >= 5:
            break
    print(f'Os numeros sorteador foram: {lista}')
def soma(lista):
    sompar = 0
    for valor in lista:
        if valor % 2 == 0:
            sompar += valor
    print(f'A soma dos numeros pares é = {sompar}', end=' ')


sorteia()
soma(lista)