def soma(a, b):
    x = a + b
    return x

def divisão(a,b):
    x = a/b
    return x


n = float(input('Digite o primeiro numero: '))
n1 = float(input('Digite o segundo número: '))
opc = str(input('Qual operação voce deseja? '))

if opc == 'soma':
    resultdefsoma = soma(n, n1)
    print(resultdefsoma)

elif opc == 'divisao':
    resultdefdivis = divisão(n, n1)
    print(resultdefdivis)
