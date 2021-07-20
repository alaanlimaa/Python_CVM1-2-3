lista =[[], []]
for n in range(1,8):
    num = int(input(f'{n}º valor: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
print('=' * 30)
lista[0].sort()
print(f'Os números PARES são: {lista[0]}')
lista[1].sort()
print(f'Os números ÍMPARES são: {lista[1]}')
print('=' * 30)
print(' === PROGRAMA FINALIZADO === ')
