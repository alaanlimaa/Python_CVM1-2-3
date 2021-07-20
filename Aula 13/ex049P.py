'''Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for.'''

#RESOLUÇÃO ALAN
'''mult = int(input(' Digite um número para ver sua tabuada: '))
for num in range(1, 11):
    rest = num * mult
    print('{} X {} = {} '. format(num, mult, rest))'''

#RESOLUÇÃO PROFESSOR
from time import sleep
num = int(input(' Digite um número para ver sua tabuada: '))
print('PROCESSANDO. . . ')
sleep(2)
for c in range(1, 11):
    print('{} x {} = {}'.format(c, num, num * c))
    sleep(1)
sleep(1)
print('''
OBRIGADO PARCEIRO''')
