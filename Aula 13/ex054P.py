from datetime import date
atual = date.today().year
tot = 0
mtot = 0
for pessoas in range(1, 8):
    ano = int(input('Em que ano a {}º pessoa nasceu?'.format(pessoas)))
    maior = atual - ano
    print('A mesma tem {} anos'.format(maior))
    if maior >= 21:
        tot += 1
    elif maior < 21:
        mtot += 1
print('{} pessoas atingiram a maturidade'.format(tot), end='')
print(' e {} pessoas menores de idade'.format(mtot))
