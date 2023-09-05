def notas(*n, sit=False):
    '''
    -Funcao q serve para analizar a nota mais alta, a mais baixa e a media de todas colocadas
    -se preferir, pode utilizar a "situacao" para ver como esta a dituacao geral da sala
    '''
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if r['media'] >= 7:
        r['situacao'] = 'Boa'
    elif r['media'] >= 5:
        r['situacao'] = 'Razoavel'
    else:
        r['situacao'] = 'Ruim'
    return r


t = notas(3, 5, 8.4, 7,10, 10)
print(t)
help(notas)
