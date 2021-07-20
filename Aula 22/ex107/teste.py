import moeda

p = float(input('Digite o preço: '))
print(f'A metade = {moeda.metade(p)}')
print(f'O dobro = {moeda.dobro(p)} ')
print(f'Aumentando 10% = R$ {moeda.aumentar(p, 10)}')
print(f'Diminuir em 13% = R$ {moeda.diminuir(p, 13)}')