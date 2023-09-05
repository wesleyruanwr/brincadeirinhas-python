from datetime import datetime
dados = {}
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['CTPS'] = int(input('Carteira de trabalho (0 nao tem): '))
if dados['CTPS'] != 0:
    dados['Ano de contratacao'] = int(input('Ano de contratacao: '))
    dados['Salario'] = float(input('Salario: '))
    dados['Aposentadoria'] = (dados['Ano de contratacao'] + 35) - datetime.now().year 
dados['idade'] = datetime.now().year - nasc
print('-=' * 30)
for k, v in dados.items():
    print(f'- {k} tem valor {v}') 
