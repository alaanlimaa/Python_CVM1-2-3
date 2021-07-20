print('=' * 40)
print('                MEGA SENA            ')
print('=' * 40)
from random import randint
from time import sleep
jogo = []
quant = int(input('Quantos jogos deseja fazer? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            cont += 1
        if cont == 6:
            break
    jogo.sort()
    print(f'Jogo de Nº {tot} = {jogo}')
    jogo.clear()
    tot += 1
    sleep(1)
sleep(2)
print('=' * 40)
print(' ==== BOA SORTE ====')










