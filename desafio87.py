matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = col = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz [l][c] = int(input(f'Digite um valor para [{l} {c}]: '))
        if matriz [l][c] % 2 == 0:
            par += matriz [l][c]
        if l == 1:
            if c == 0:
                mai = matriz [l][c]
            else:
                if mai < matriz [l][c]:
                    mai = matriz [l][c]
for l in range(0, 3):
            col += matriz [l][2]   #Fixei a coluna na 2 e li apenas as linhas
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'A soma do valores pares é de {par}')
print(f'A soma dos valores da terceira coluna é de {col}')
print(f'O maior valor da segunda linha é {mai}')
