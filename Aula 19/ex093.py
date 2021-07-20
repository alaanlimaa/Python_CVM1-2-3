from random import randint
from time import sleep
dados = {}
lista = []
dados['Nome'] = str(input('Nome do jogador: ')).title()
dados['Partidas'] = int(input('Número de partidas jogadas: '))
somagols = 0
for c in range(1, dados['Partidas']+1):
    gols = randint(0, 3)
    lista.append(gols)
    print(f'Partida {c} o jogador fez {gols} gol(s)!')
    somagols += gols
dados['Gols'] = lista
dados['Total'] = somagols
print(' ===== APROVEITAMENTO POR PARTIDA =====  ')
print(dados)
print('=' * 40)
for k, v in dados.items():
    if k == 'Total':
        print(f'  -O {k} de gols marcados no campeonado é {somagols}')
    else:
        print(f'  -{k} = {v}')
    sleep(1)
print()
print('PROGRAMA FINALIZADO')
