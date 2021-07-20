'''Exercício Python 28: Escreva um programa que faça o computador “pensar” em um
número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o
número escolhido pelo computador.  O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

# PROGRAMA ABAIXO DESENVOLVIDO POR MIM'''
'''from random import randint
n = randint(0,5)
u = int(input('Qual foi o número escolhido pelo computador, de 0 à 5? : '))
if n == u:
    print('Você acertou')
else:
    print('Você errou')
print('O numero escolhido pelo computador foi {}'.format(n))'''

# RESOLVIDO PELO PROFESSOR
from random import randint
from time import sleep   #SLEEP FAZ O COMPUTAR DORMIR/ESPERAR POR ALGUNS SEGUNDOS
cpu = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
gamer = int(input('Em qual número pensei? '))
print('PROCESSANDO...')
sleep(3) #COLOQUE ENTRE () O TEMPO QUE DESEJA
if gamer == cpu:
    print('PARABÉNS! Você me venceu')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(cpu, gamer))
