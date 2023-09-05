ex = str(input('Digite a expressão: '))
lista = []
for simb in ex:
    if simb in '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
                lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
     print('Expressao invalida!')
else:
     print('Expressao valida!')
