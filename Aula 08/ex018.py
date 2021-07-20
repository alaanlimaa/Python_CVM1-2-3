# FORMA 1 DE RESOLUÇÃO
'''import math
an = float(input('Digite um angulo  Xº: '))
seno = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print('Conforme angulo digitado, o valor de seno é {}, de cosseno é {} e a tangente é {}!'.format(seno, cos, tan))'''

# FORMA 2 DE RESOLUÇÃO
from math import sin, cos, tan, radians
an = float(input('Digite um angulo: '))
seno = sin(radians(an))
cos = cos(radians(an))
tan = tan(radians(an))
print('O angulo de {} tem SENO de {:.2f}, COSSENO de {:.2f} e TANGENTE de {:.2f}'.format(an, seno, cos, tan))

