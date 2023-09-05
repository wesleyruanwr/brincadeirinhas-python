import moeda
num = float(input('Digite um numero: '))
print(f'{moeda.moeda(num)} com aumento de {10}% é {(moeda.aumento(num, 10, True))}')
print(f'{moeda.moeda(num)} com diminuição de {15}% é {(moeda.diminui(num, 15, True))}')
print(f'o dobro de {moeda.moeda(num)} é {(moeda.dobro(num, True))}')
print(f'a metade de {moeda.moeda(num)} é {(moeda.metade(num, True))}')

#adiciono um parâmetro para o programa saber se deve ou não colocar o resultado na formatação