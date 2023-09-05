dados = {}
lista = []
dados['nome'] = str(input('Nome do jogador: '))
part = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for c in range(0, part):
    n = int(input(f'Quantos gols {dados["nome"]} fez no {c+1} jogo? '))
    lista.append(n)
dados['gols'] = lista[:]
dados['total'] = sum(lista)
print('-=' *30)
print(dados.items())
print('-=' *30)
for k, v in dados.items():
    print(f'campo {k} tem valor {v}')
print('-=' *30)
c = 0
i = 0
print(f'O jogador {dados["nome"]} jogou {part} partidas') #se usasse "len(jogador["gols"]) tambem iria ler a quantidade de partidas que ele fez gols"
while True:
    print(f'-- Na partida {c+1}, fez {lista[i]} gols')
    c += 1
    i += 1
    if c == part:
        break
print(f'Ao todo foram {[dados["total"]]} gols')
