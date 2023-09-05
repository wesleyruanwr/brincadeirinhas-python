def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31merro! Digite um numero inteiro valido.\033[m')
        if ok == True:
            break
    return n

n = (leiaint('Digite um numero: '))
print(f'voce digitou o numero {n}')
