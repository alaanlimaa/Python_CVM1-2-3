soma = maior1000 = cont = menor = 0
barato = ' '
while True:
    produto = str(input('Produto nome: ')).strip()
    cont += 1
    valor = float(input('Valor: R$ '))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    print('-=-' * 15)
    if valor > 0:
        soma += valor
    if valor > 1000:
        maior1000 += 1
    if cont == 1 or valor < menor:
        menor = valor
        barato = produto
    if resp == 'N':
        break
print('PROGRAMA FINALIZADO.!')
print(f'O total gasto foi de R$ {soma:.2f}')
print(f'Foram cadastrados {maior1000} produtos com valor superior a R$ 1000.00')
print(f'O produto mais barato foi o(a) {barato} e custa R$ {menor}')


