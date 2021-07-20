print('-=-' * 10)
print('   ANALISANDO UM TRIÂNGULO')
print('-=-' * 10)
r1 = float(input('Comprimento da PRIMEIRA reta: '))
r2 = float(input('Comprimento da SEGUNDA reta: '))
r3 = float(input('Comprimento da TERCEIRA reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo', end='')
    if r1 == r2 == r3:
        print(' EQUILÁTERO')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print(' ISÓSCELES')
    else:
        print(' ESCALENO')
else:
    print('Não forma um triângulo')
