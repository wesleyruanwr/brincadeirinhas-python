def voto(a=0):
    from datetime import date   #colocando a biblioteca dentro do DEF apenas voce deixa o escopo limitado, economizando memoria
    idade = date.today().year - a
    if 17 >= idade >= 16 or idade >= 65:
        return f'com {idade} anos seu voto e facultativo'
    if 59 >= idade >= 18:
        return f'com {idade} anos seu voto e obrigatorio'
    if idade < 16:
        return f'com {idade} anos voce ainda nao pode votar'    


a = int(input('Digite seu ano de nascimento: '))
print(voto(a))