def ajuda(h):
    help(h)


#programa principal
opc = ''
while True:
    ajuda(input('funcao ou biblioteca: '))
    opc = str(input('deseja continuar? [S/N]: '))
    if opc == 'N':
        break
    else:
        ajuda(input('funcao ou biblioteca: '))
print('Fim, ate logo')