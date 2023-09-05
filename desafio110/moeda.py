def metade(n=0, format=False):
    res = n/2
    return res if format is False else moeda(res)


def dobro(n=0, format=False):
    res = n*2                                             
    return res if format is False else moeda(res)       


def aumento(n=0, t=0, format=False):
    res = n + (n* (t/100))
    return res if format is False else moeda(res)


def diminui(n=0, t=0, format=False):
    res = n - (n * (t/100))
    return res if format is False else moeda(res)


def moeda(n=0, moeda='R$', x='Não'):
    return f'{moeda}{n:.2f}'.replace('.', ',')


def resumo(n=0, taxaa=10, taxar=5):
    print('-'*35)
    print('RESUMO DO VALOR'.center(35)) #centralizado em 30 caracteres
    print('-'*35)
    print(f'preço analizado: \t{moeda(n)}')
    print(f'{taxaa}% de aumento: \t{aumento(n, taxaa, True)}')      #o "\t" é para mostrar os resultados tabulados
    print(f'{taxar}% de diminuição: \t{diminui(n, taxar, True)}')   #na msm linha bonitinhos
    print(f'o dobro do valor: \t{dobro(n,True)}')
    print(f'a metade do valor: \t{metade(n,True)}')
    print('-'*35)
