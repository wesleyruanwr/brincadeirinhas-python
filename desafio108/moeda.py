def metade(n=0):
    return n/2


def dobro(n=0):
    return n*2


def aumento(n=0, t=0):
    res = n + (n* (t/100))
    return res


def diminui(n=0, t=0):
    res = n - (n * (t/100))
    return res


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')
        #retorna o simbolo "R$" junto com o valor de N formatado em 2 espacos
        #e troca o "." por "," ja que no padrao americano do python ele usa o
        #ponto ao invés de virgula