import moeda
num = float(input('Digite um numero: '))
print(f'{num} com aumento de {10}% é {moeda.aumento(num, 10)}')
print(f'{num} com diminuição de {15}% é {moeda.diminui(num, 15)}')
print(f'o dobro de {num} é {moeda.dobro(num)}')
print(f'a metade de {num} é {moeda.metade(num)}')