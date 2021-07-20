import moeda

p = float(input('Digite o preço: '))
print(f'A metade = {moeda.metade(p, True)}')
print(f'O dobro = {moeda.dobro(p, True)} ')
print(f'Aumentando 10% = {moeda.aumentar(p, 10, True)}')
print(f'Diminuir em 13% = {moeda.diminuir(p, 13, True)}')