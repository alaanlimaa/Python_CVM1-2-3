lista = []
while True:
    n = int(input('Digite um número: '))
    if n not in lista:
        lista.append(n)
    else:
        print('O número ja está na lista! EXCLUINDO!!!')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=-' * 20)
lista.sort()
print(f'A lista ficou ►►► {lista}')
maior = max(lista)
menor = min(lista)
print(f'O maior é {maior} na posição ', end='')
for p, v in enumerate(lista):
    if v == maior:
        print(f'{p}', end=' ')
print(f'\nO menor é {menor} na posição ', end='')
for p, v in enumerate(lista):
    if v == menor:
        print(f'{p}', end=' ')