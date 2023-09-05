'''Aula de listas'''
'''Lsitas são Mutáveis'''
''' ".append('')" adiciona um elememtno no final da lista'''
''' ".insert('')"  adiciona um elemento no local da lista predefinido'''
'''maneiras de eliminar um elemento da lista'''
''' "del lanche [3]" ou "lanche.pop(3)"  ou ".remove('valor')" '''
''' o comando ".sort()" coloca os elementos da lista em ordem '''
''''Se quiser em orden inversa basta fazer ".sort(reverse=True)" '''
                                                    #com T maiusulo
valores = []
valores.append(5)
valores.append(9)
valores.append(6)

for cont in range(1, 5):
    valores.append(int(input('Digite um número: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} eu encontrei o número {v}')

a = [2, 6, 5, 8]
b = a [:] #para copiar uma lista para outra
b[2] = 9
print(f'lista A: {a}')
print(f'lista B: {b}')
