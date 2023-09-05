time = 'Palmeiras', 'intenacional', 'fluminese', 'corinthias', 'flamengo', 'athletico-pr', 'atlético-mg', 'fortaleza', 'são paulo', 'américa-mg', 'botafogo', 'santos', 'goias', 'bragantino', 'coritiba', 'cuiaba', 'ceara', 'atletico-go', 'avai', 'juventude'
print(f'os times do brasileirão são {time}')
print(f'os 5 primeiros colcados são {time[:5]}')
print(f'os 4 ultimos colocados são {time[-4:]}')
print(f'Em ordem alfabetica fica: {sorted(time)}')
print(f'O Fortaleza está na {time.index("fortaleza")+1}ª colocação')