maior = menor = 0
lista = []
for cont in range(0,5):
    lista.append(int(input(f'Digite um valor na posição {cont}: ')))
    if cont == 1:
        menor = maior = lista[cont]
    if lista[cont] > maior:
        maior = lista[cont]
    if lista[cont] < menor:
        menor = lista[cont]
print('=-'*30)
print(f'Voce digiou os numeros {lista}')
print(f'O maior valor digitado foi o {maior} na posições', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f' {i}')
print(f'O menor valor digitado foi o {menor} na posições ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}', end='')

