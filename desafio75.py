num = (int(input('Digite um número: ')),
      int(input('Digite outro número: ')),
      int(input('Digite mais um número: ')),
      int(input('Digite o último número: ')))
print(f'O número 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O primeiro número "3" apareceu na {num.index(3) +1}ª posição.')
else:
    print('O valor "3" n foi digitado em nenhuma posição')
print('Os valores pares foram: ', end='')
for n in num:
    if n % 2  == 0:
        print(f'{n}', end=' ')
