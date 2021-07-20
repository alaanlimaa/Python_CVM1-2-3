times = ('Flamengo', 'Internacional', 'Atletico-MG', 'São Paulo',
         'Fluminense', 'Grêmio', 'Palmeiras', 'Santos', 'Athletico-PR',
         'Bragantino', 'Ceara', 'Corinthians', 'Atletico-GO', 'Bahia',
         'Sport', 'Fortaleza', 'Vasco', 'Goias', 'Coritiba', 'Botafogo')
print(f'Os 5 primeiros times são {times[0:5]}')
print('-=-' * 20)
print(f'Os últimos 4 colocadas são {times[-4:]}')
print('-=-' * 20)
print(sorted(times))
print('-=-' * 20)
print(f'O São Paulo está na {times.index("São Paulo")+1}ª posição!')
