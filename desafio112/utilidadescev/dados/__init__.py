def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input('Digite um valor: R$ ')).strip
        if entrada.isalpha() or entrada == '':
            print(f'\033[31m{entrada} não é um valor válido, tente novamente\033[m')
        else:
            valido = True
            return float(entrada)
