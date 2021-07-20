#FORMA 1 DE RESOLUÇÃO:
'''from math import factorial
n = int(input('Digite um número:'))
f = factorial(n)
print('O factorial de {} é {}'.format(n, f))'''

#FORMA 2 DE RESOLUÇÃO:
'''from math import factorial
n = int(input('Digite um número:'))
c = n
print('{}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = {}'.format(f), end='')
    c -= 1
    f = factorial(n)'''

#FORMA 3 DE RESOLUÇÃO:
'''n = int(input('Digite um número:'))
c = n
f = 1
print('{}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = {} '.format(f), end='')
    f *= c
    c -= 1'''

#FORMA 4 DE RESOLUÇÃO:
from math import factorial
n = int(input('Digite um número:'))
for c in range(1, n + 1):
    print('{}'.format(c), end='')
    print(' x ' if c < n else ' = {}'.format(f), end='')
    f = factorial(n)
print('\nObrigado')















