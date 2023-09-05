lista = []
c5 = 0
opc = ''
while True:
    n = int(input('Digite um numero: '))
    lista.append(n)
    if n == 5:
        c5 += 1
    opc = str(input('Deseja adicionar mais um numero? [S/N]:')).strip()[0]
    if opc in 'Nn':
        break
print('=-' *30)
print(f'Foram digitados {len(lista)} numeros')
print(f'O numero 5 foi digitado {c5} vezes')
lista.sort(reverse=True)
print(f'A lista em ordem decrecente ficou {lista}')
