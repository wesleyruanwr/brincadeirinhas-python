def metade(n=0, format=False):
    res = n/2
    return res if format is False else moeda(res)


def dobro(n=0, format=False):
    res = n*2                                             
    return res if format is False else moeda(res)       #a def vai retornar apenas o RES se o format for falso, que é o padrao
                                                        #se colocar no programa principal como True, ele chama a funcao "moeda"
                                                        #e formata o resultado nela
def aumento(n=0, t=0, format=False):
    res = n + (n* (t/100))
    return res if format is False else moeda(res)


def diminui(n=0, t=0, format=False):
    res = n - (n * (t/100))
    return res if format is False else moeda(res)


def moeda(n=0, moeda='R$', x='Não'):
    return f'{moeda}{n:.2f}'.replace('.', ',')
