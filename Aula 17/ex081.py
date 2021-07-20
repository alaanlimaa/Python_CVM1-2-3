lista = []
cont = 0
while True:
    num = int(input('Digite um número: '))
    cont += 1
    lista.append(num)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
print('-=-' * 20)
print(f'Foram digitados {cont} números!!')
print(f'A lista ficou : {sorted(lista, reverse=True)}')
if 5 in lista:
    print('O valor 5 ESTÁ na Lista!')
else:
    print('O valor 5 NÃO esta na lista!')

