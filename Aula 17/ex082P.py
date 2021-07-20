valores = []
pares = []
impares = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer sontinuar? [S/N]: '))
    if resp in 'Nn':
        break
for p, v in enumerate(valores):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('-=-' * 20)
print(f'A lista completa →→ {valores}')
print(f'A lista de pares →→ {pares}')
print(f'A lista de impares →→ {impares}')

