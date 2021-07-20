from random import randint
from time import sleep
jogadores = {}
for p in range(1, 5):
    num = randint(1, 6)
    jogadores[f'Jogador[{p}]'] = num
for k, v in jogadores.items():
    print(f'O {k} tirou {v} no dado!')
    sleep(1)
print()
print('=' * 15, 'RANKING', '=' * 15)
print()
cont = 0
for k, v in sorted(jogadores.items(), key= lambda item: item[1], reverse=True):
    cont += 1
    print(f'{cont}º Lugar = {k} com valor de {v}')
    sleep(1)
