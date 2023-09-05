#Aula de Funcoes
#DEF = definicao de funcoes
#funcoes sao rotinas, coisas q acontecem repetidamente

def mensagem(txt):
    print('-'*30)
    print(txt)
    print('-'*30)
                    #python sempre pede 2 linhas entre uma DEF e o programa principal

mensagem('python e bom')
mensagem('vou ser um grande programador')
mensagem('vou vencer')

def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')


soma(3, 5)
soma(9, 2)
soma(a = 4, b = 0)    #posso explicitar ou nao quem e o A e B


#O asteristico antes de NUM e o simbolo de desempacotar
#Independente da quantidade de numerois que eu colocar ele vai ler e colocar em num
#se colocar 3 ele vai dizer 3, se colocar 5 diz 5, e assim vai
def contador(*num):
    tam = len(num)
    print(f'recebi os valores {num} e ao todo sao {tam} numeros')
 

contador(0, 4, 1, 7, 3)
contador(6, 7)

def elementos(*num):
    print(num)


elementos(3, 4, 7, 9)
elementos(1, 4, 9, 0, 2)

#trabalhando com listas q diferente das tuplas sao mutaveis
def dobra(lst):
    posicao = 0
    while posicao < len(lst):
        lst[posicao] *= 2
        posicao += 1


ele1 = [3, 5, 7]
ele2 = [4, 6, 8, 1, 2, 0, 3]
dobra(ele1)
dobra(ele2)
print(ele1)
print(ele2)
