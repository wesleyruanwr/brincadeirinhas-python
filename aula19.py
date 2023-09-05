#Dicionários se usa '{} ou dict()'
pessoas = {'nome': 'wesley', 'idade': 19, 'sexo': 'M'}
pessoas.keys() #mostra as variaveis ''nome...idade...sexo''
pessoas.values() #mostra os valores das variaveis ''wesley...19...M''
pessoas.items() #mostra variaveis e valores juntos

for k in pessoas:
    print(k)  #vai mostrar as keys

for k, v in pessoas.items():
    print(f'O {k} é {v}')

del pessoas['sexo'] #elimina não só o valor mas a variavel também
                    #ficando apenas 'nome' e 'idade' no dicionario
                
pessoas['nome'] = 'ruan' #se pode trocar a variavel de uma chave dessa forma
pessoas['peso'] = 74 #como também se pode adicionar

brasil = []
estado1 = {'uf': 'pernambuco', 'sigla': 'PE' }
estado2 = {'uf': 'Ceara', 'sigla': 'CE'}
brasil.append(estado1, estado2)   #dessa forma adiciona o dicionario dentro da lista

brasil = []
estados = {}
for c in range(0, 3):
    nomestado = str(input('Digite o nome do estado: '))
    uf = str(input('Digite o UF do estado: '))
    brasil.append(estados.copy()) #serve como o "[:]" em listas
print(brasil)