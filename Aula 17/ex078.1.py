lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    lista.append(n)
print('-=-' * 20)
print(f'A lista ficou →→ {lista}')
print('-=-' * 20)
maior = max(lista)
menor = min(lista)
print(f'O maior valor foi {maior} e está na posição ', end='')
for p, v in enumerate(lista):
    if v == maior:
        print(f'{p}', end=' ')
print(f'\nO menor valor foi {menor} e está na posição ', end='')
for p, v in enumerate(lista):
    if v == menor:
        print(f'{p}', end=' ')



