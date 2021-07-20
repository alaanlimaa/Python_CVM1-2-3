def line(msg):
    print('=' * (len(msg) + 4))
    print(f'\033[1;34m{msg.center(len(msg) + 4)}\033[m')
    print('=' * (len(msg) + 4))


line('ANALISANDO UM TRIÂNGULO')
r1 = float(input('Comprimento PRIMEIRA reta: '))
r2 = float(input('Comprimento SEGUNDA reta: '))
r3 = float(input('Comprimento TERCEIRA reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo')
    if r1 == r2 == r3:
        print('É um triângulo EQUILÁTERO!')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('É um triângulo ISÓSCELES!')
    elif r1 != r2 != r3:
        print('É um triângulo ESCALENO!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')