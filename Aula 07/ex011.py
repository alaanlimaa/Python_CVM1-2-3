l = float(input('Qual é a largura da parede (m): '))
a = float(input('Qual é a altura da parede (m): '))
area = a * l
print('Sabendo que 1 litro de tinta pinta aproximadamente uma área de 2m²')
print('Sua parede tem um total de {:.2f}m²'.format(area))
print('Sendo assim, são necessários {:.2f} litros de tinta'.format(area/2))

