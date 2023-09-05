aluno = dict() #ou so usa chaves "{}"
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'media de {aluno["nome"]}: '))
print(f'O nome e {aluno["nome"]}')
print(f'A media dele e {aluno["media"]}')
if aluno["media"] >= 7:
    print('A situacao e aprovado')
elif 6.9 >= aluno["media"] >= 6:
    print('Aa situacao e recuperacao')
else:
    print('A situacao e reprovado') 