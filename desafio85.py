princ = [[], []]
for c in range(0,7):
    num = int(input(f'Digite o {c} valor: '))
    if num % 2 == 0:
        princ[0].append(num)
    else:
        princ[1].append(num)
princ[0].sort()
princ[1].sort()
print(f'Os valores pares digitados foram {princ[0]}')
print(f'Os valores impares digitados foram {princ[1]}')
