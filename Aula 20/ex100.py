from random import randint
from time import sleep
def sorteia(valores):
    lista = []
    print(f'Sorteando {valores} valores da lista: ', end='')
    for c in range(1, valores + 1):
        num = randint(1, 10)
        print(f'{num} ', end='')
        sleep(0.4)
        lista.append(num)
    print(' PRONTO!')





sorteia(5)






