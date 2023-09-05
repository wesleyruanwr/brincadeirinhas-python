def fatorial(num=0, show=False):
    """
    --Calcula o fatorial de um Numero
    num = parametro que recebe o numero a ser fatorado
    show = parametro que dita se o utilizador deseja ver a conta que foi feita para chegar ao resultado
    return = retorna o valor final da resposta
    """
    cont = resp = 1
    for c in range(num, 0, -1):
        if show:
            print (c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        resp *= c
    return resp


final = fatorial(4, show=True) 
print(final)

