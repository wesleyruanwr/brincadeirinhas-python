tup = 'celular', 'fone', 'relógio', 'mouse', 'alfáce'
for c in tup:
    print(f'\nNa palavra {c} temos: ', end='') #\n é para quebrar a linha
    for letra in c:
        if letra in 'aáâãeéêiíoôõuú':
            print(letra.lower(), end='')
