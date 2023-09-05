import moeda
num = float(input('Digite um numero: '))
print(f'{moeda.moeda(num)} com aumento de {10}% é {moeda.moeda(moeda.aumento(num, 10))}')
print(f'{moeda.moeda(num)} com diminuição de {15}% é {moeda.moeda(moeda.diminui(num, 15))}')
print(f'o dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}')
print(f'a metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}')
                            #o primeiro moeda é do arquivo, o segundo é da função para formatação
                            #o terceiro de dentro dos parenteses é referente a qual função do arquivo moeda
                            #ele irá usar