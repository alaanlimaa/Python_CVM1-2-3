from random import randint
from time import sleep
while True:
    jogador = int(input('Digite um número: '))
    comp = randint(0, 10)
    total = jogador + comp
    tipo = ' '
    v = 0
    while tipo not in 'PI':
        tipo = str(input('O queseja ÍMPAR OU PAR? [I/P]')).strip().upper()[0]
        while tipo not in 'PI':
            tipo = str(input('O queseja ÍMPAR OU PAR? [I/P]')).strip().upper()[0]
        print(f'Você falou {jogador} e o computador {comp} , total = {total}', end=' ')
        print(' DEU PAR!!!' if total % 2 == 0 else 'DEU ÍMPAR!!')
        sleep(2)
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU!')
            v += 1
        else:
            print('VOCÊ PERDEU!!')
            break
    if tipo == 'I':
        if total % 2 != 0:
            print('VOCÊ VENCEU!')
            v += 1
        else:
           print('VOCÊ PERDEU!')
           break
print(f'Você teve {v} vitórias consecutivas !!')

