#parte 2 de def

#interactive help 
    
    #no console do python ou direto no codigo voce pode usar o "help()" para obter a lista de funcionalidades
    #de todas as coisas do python

#outra forma é usar o DOC, por exemplo -- "print(input.__doc__)", isso ira mostrar as funcoes do input

#DOCSTRINGS
    
    #serve para ser um manual de uma funcao que voce tenha criado para se outra pessoa quiser saber
    #o que faz basta colocar no help para saber, por exemplo se voce criar uma funcao contador
    #quem quiser saber o que faz basta colocar help(contador), mas para isso funcionar precisa
    #abrir aspas dulpas 3 vezes na linha debaixo da DEF
    
#PARAMETROS OPICIONAIS
def somar(a=0, b=0, c=0): #se nao for adicionado nenhum valor em alguma das variaveis, o programa usa o valor 0
    s = a+b+c
    print(f'A soma dos valores e {s}')

#ESCOPO DE VARIAVEIS
    
    #indica ate onde no codigo uma variavel e valida

#RETORNO DE VALORES "return"

def somar(a=0, b=0, c=0):
    s = a+b+c
    return s    #com o return eu consigo personalizar minha frase em baixo
    
r1 = somar(2, 5, 7)
r2 = somar(9, 4)
r3 = somar(1, 0, 2)
print(f'os resultados foram {r1}, {r2}, {r3}')
