'''Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.'''

#RESOLUÇÃO ALAN
'''print('Os números pares são:')
for num in range(1, 50):
    cal = num % 2
    if cal == 0:
        print(num)
print('OBRIGADO')'''

#RESOLUÇÃO PROFESSOR forma 1
'''for n in range(1, 51):
    if n % 2 == 0:
        print(n, end=' ')
print('Acabou')'''

#RESOLUÇÃO PROFESSOR forma 2
for n in range(2, 51, 2):
    print('.', end='')
    print(n, end=' ')
print('ACABOU!!!')

