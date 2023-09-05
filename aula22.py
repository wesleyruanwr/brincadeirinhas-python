# MODULARIZAÇÃO

def fat(n):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f


num = int(input('digite um numero: '))
fat(num)
print(f'o fatorial do numero {num} é {fat(num)}')