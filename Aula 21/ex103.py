def ficha(n='<desconhecido>', g=0):
    print(f'O jogador {n} fez {g} gol(s) na temporada!')

nome = str(input('Nome jogador: ')).title().strip()
gols = str(input('Número de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(g=gols)
else:
    ficha(nome, gols)
