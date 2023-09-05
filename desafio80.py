lista = []
for c in range(0, 5):
    n = int(input('Digite um numero: '))
    if c == 0 or n > (lista[len(lista) - 1]): #pode ser escito apenas com -- lista[-1]
        lista.append(n)
        print('Adicionado no fim da lista' )
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição: {pos}')
                break
            pos += 1
print(lista)