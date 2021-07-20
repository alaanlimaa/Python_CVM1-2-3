'''Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.'''

# MINHA RESOLUÇÃO
num = int(input('Digite um número inteiro: ')) #FALTOU O INT DE INTEIRO, POR ISSO NÃO DEU CERTO
div = num % 2
if div == 0:
    print('O numero {} é par'.format(num))
else:
    print(' O número {} é ímpar'.format(num))

