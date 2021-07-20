from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10),
     randint(1, 10), randint(1, 10))
print(f'Eu sorteei os números {n} ')
print(f'O maior valor sorteado é {max(n)}')
print(f'O menor valor sorteado é {min(n)}')