lista = []
cont = 0
while True:
    num = int(input('Digite um valor:'))
    cont += 1
    if num not in lista:
        lista.append(num)
    else:
        print('Número ja existe na lista! Excluindo...')
    resp =' '
    while resp not in 'SN':
        resp = str(input('Deseja continua [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=-' * 5)
#print(f'A lista foi :{sorted(lista)}')  - - -  FORMA 1 DE ORGANIZAÇÃO
lista.sort()
print(f'A lista foi: {lista}')






