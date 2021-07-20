from random import randint
jogador = {}
listagols = []
time = []
while True:
    jogador['Nome'] = str(input('Nome: ')).title()
    jogos = int(input('Quantidades de partidas: '))
    somagols = 0
    for p in range(1, jogos + 1):
        gols = randint(1, 3)
        listagols.append(gols)
        somagols += gols
        print(f'   Na partida {p} fez {gols} gols!')
    jogador['Gols'] = listagols[:]
    jogador['Total'] = somagols
    time.append(jogador.copy())
    listagols.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 30)
print('Cod. ', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('--' * 30)
for i, v in enumerate(time):
    print(f'{i:<3} ', end='')
    for d in v.values():
        print(f'{str(d):<15} ', end='')
    print()
print('==== DADOS INDIVIDUAIS ===')
while True:
    busca = int(input('Qual jogador deseja avaliar? [999 break]: '))
    if busca == 999:
        break
    if busca > len(time):
        print('ERRO! Jogador não existe!!!')
    else:
        print(f'==== JOGADOR {time[busca]["Nome"]}:')
        for i, g in enumerate(time[busca]['Gols']):
            print(f'   - Na partida {i+1} fez {g} gols! ')
print('PROGRAMA FINALIZADO')









