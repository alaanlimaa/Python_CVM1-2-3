'''num = int(input('Digite um valor: '))
n = num + 1
f = 1
print(f'{num}! = ', end='')
while n > 1:
    n -= 1
    f *= n
    print(n, end=' ')
    print('x ' if n > 1 else f'= {f}', end='')
print('\nACABOU')'''

from math import factorial
num = int(input('Digite um valor: '))
for c in range(1, num + 1):
    print(f'{c}', end=' ')
    print('x' if c < num else f'= {factorial(num)}', end=' ')
print('\nOBRIGADO')
