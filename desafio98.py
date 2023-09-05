from time import sleep
def contador(a, b, c):
    print(f'Contagem de {a}, até {b} de {c} em {c}')
    if a < b:
        r = a
        while r <= b:
            print(f'{r} ', end='', flush=True)
            sleep(0.5)
            r += c
    else:                           #Flush é para impedir q a contagem do sleep so apareca depois de calcular todos
        r = a
        while r >= b:
            print(f'{r} ', end='', flush=True)
            sleep(0.5)
            r -= c
    print('FIM')

contador(1, 10, 1)
contador(10, 0, 2)
print('Sua vez de personalizar a contagem!')
while True:
    ini = int(input('Inicio: '))
    fim = int(input('Fim: '))
    pas = int(input('passo: '))
    contador(ini, fim, pas)
    opc = str(input('Deseja continuar? [s/n] ')).strip().upper()[0]
    if opc == 'N':
        print('Finalizando...')
        break