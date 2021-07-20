listageral = []
listapares = []
listaimpares = []
while True:
    num = (int(input('Digite um valor: ')))
    listageral.append(num)
    if num % 2 == 0:
        listapares.append(num)
    else:
        listaimpares.append(num)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=-' * 20)
print(f'A lista geral ficou: {listageral}')
print(f'A lista de números pares é {listapares}')
print(f'A lista de números impares é {listaimpares}')
