from random import randint #errei aqui
from time import sleep
itens = ('Papel', 'Tesoura', 'Pedra') #dúvida aqui
computador = randint(0, 2) #dúvida aqui
print('''Escolha um das opções abaixo:
[ 0 ] Papel
[ 1 ] Tesoura
[ 2 ] Pedra''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
sleep(1)
print('-=' * 20)
print('O computador escolheu {}'.format(itens[computador])) #atenção
print('O jogador escolheu {}'.format(itens[jogador])) #atenção
print('-=' * 20)
if computador == 0: #PAPEL
    if jogador == 0:
        print('JOGADA EMPATADA')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
elif computador == 1: #TESOURA
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('JOGADA EMPATADA')
    elif jogador == 2:
        print('JOGADOR VENCEU')
elif computador == 2: #PEDRA
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('JOGADA EMPATADA')
else:
    print('JOGADA INVÁLIDA')
