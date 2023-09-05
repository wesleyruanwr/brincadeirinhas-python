c = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
opc = ''
while opc in 'Ss':
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if num >= 0 and num <= 20:
            break
        print('tente novamente.')
    print(f'Você digitou o número {c[num]}')
    opc = str(input('Você quer continuar? [S/N]' ))
print('Fim do programa')
