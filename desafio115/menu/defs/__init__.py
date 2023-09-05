def numenu(n):
    try:
        num = int(input(n))
    except (ValueError, TypeError):
        print('Por favor digite um número inteiro válido')
    else:
        return n