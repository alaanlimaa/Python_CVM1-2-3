from random import randint
print('-=' * 13)
print('VAMOS JOGAR PAR OU IMPAR')
print('-=' * 13)
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    comp = randint(0, 10)
    total = jogador + comp
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Pau ou Ímpar? [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {comp}. Total de {total}!', end='')
    print(' DEU PAR!!!' if total % 2 == 0 else ' DEU ÍMPAR!!!')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 != 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente . . . ')
    print('-=' * 20)
print('-=' * 20)
print(f'!!!GAME OVER!!! Você venceu {v} vezes.' )


