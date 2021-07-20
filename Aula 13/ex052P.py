'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\33[33m', end=' ')
        tot += 1
    else:
        print('\33[31m', end=' ')
    print('{} '.format(c), end=' ')
print('\n\33[m O número {} foi dividido {} vezes!'.format(num, tot)) #\n para ficar na próxima linha e o \33 não manter a cor
if tot == 2:
    print('É por isso que o mesmo é PRIMO!!!')
else:
    print('É por isso que o mesmo NÃO É PRIMO!!!')





