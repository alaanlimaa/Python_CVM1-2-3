def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato')


n = str(input('Nome do Jogador: '))
g = str(input('Qtd. de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '': #SE O COMPUTADOR RETIROU TODAS OS ESPAÇOS E FICOU SEM NADA '', A FICHA VAI SER MOSTRADA DIFERENTE
    ficha(gol=g)
else:
    ficha(n, g)
