matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = somacol3 = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor na posição [{l}, {c}]: '))
print('=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
        if c == 2:
            somacol3 += matriz[l][2]
        if matriz[l][c] == matriz[1][0]:
            maior = matriz[1][0]
        elif matriz[1][c] > maior:
            maior = matriz[1][c]
    print()
print('=' * 30)
print(f'A soma dos números pares é {somapar}')
print(f'A soma da terceira coluna é {somacol3}')
print(f'O maior valor da segunda linha é {maior}')

