# FORMA 1 DE RESOLUÇÃO
'''import random
al1 = str(input('Digite o número do aluno 1: '))
al2 = str(input('Digite o número do aluno 2: '))
al3 = str(input('Digite o número do aluno 3: '))
al4 = str(input('Digite o número do aluno 4: '))
lista = (al1, al2, al3, al4)
escolhido = random.choice(lista)
print('O aluno(a) eschilido(a) foi o(a) {} ! '.format(escolhido))'''

# FORMA 2 DE RESOLUÇÃO
from random import choice
al1 = str(input('Digite o número do aluno 1: '))
al2 = str(input('Digite o número do aluno 2: '))
al3 = str(input('Digite o número do aluno 3: '))
al4 = str(input('Digite o número do aluno 4: '))
lista = (al1, al2, al3, al4)
escolhido = choice(lista)
print('O aluno(a) escolhido(a) foi o(a) {} ! '.format(escolhido))