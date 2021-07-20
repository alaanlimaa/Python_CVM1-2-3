num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\33[33m', end=' ')
        tot += 1
    else:
        print('\33[31m', end=' ')
    print(c, end=' ')
print(f'\n\33[mO número {num} foi dividido {tot} vezes, por isso ele é PRIMO!')
if tot == 2:
    print('Por isso ele é PRIMO!')
else:
    print('Por isso ele NÃO É PRIMO')
