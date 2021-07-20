import moeda

p = float(input('Digite o preço: '))
print(f'A metade = {moeda.moeda(moeda.metade(p))}')
print(f'O dobro = {moeda.moeda(moeda.dobro(p))} ')
print(f'Aumentando 10% = {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Diminuir em 13% = {moeda.moeda(moeda.diminuir(p, 13))}')