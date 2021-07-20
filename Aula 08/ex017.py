#PRIMEIRA FORMA DE RESOLUÇÃO
'''import math
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
print('Sendo o cateto oposto {} e o cateto adjacente {}, o valor da hipotenusa é {:.2f} !'.format(co, ca, math.hypot(co,ca)))'''

#FORMA MATEMÁTICA
'''co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co**2 + ca**2)**(1/2)
print('A hipotenusa vale {:.2f} !'.format(hi))'''

#SEGUNDO FORMA DE RESOLUÇÃO
from math import hypot
co = float(input('Catet0 oposto:'))
ca = float(input('Cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa é {:.2f} !'.format(hi))


