def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except Exception as erro:
            print(f'\033[0;31mOcorreu um erro do tipo {erro.__class__}, tente novamente\033[m ')
            continue
        else:
            return n
def leiafloat(msg):
    while True:
        try: 
            n = float(input(msg))
        except Exception as erro:
            print(f'\033[0;31mOcorreu um erro do tipo {erro.__class__}, tente novamente\033[m')
        else:
            return n
n = (leiaint('Digite um numero inteiro: '))
n1 = (leiafloat('Digite um numero real: '))
print(f'o numero inteiro foi: {n}')
print(f'O numero real foi: {n1}')
