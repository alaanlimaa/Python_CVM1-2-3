'''teste = []
teste.append('Alan')
teste.append(26)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 56
galera.append(teste)
print(galera)'''

'''galera = [['Alan', 26], ['Maria', 56], ['Aline', 29], ['Levi', 55]]
for p in galera:
    print(f'A idade de {p[0]} é {p[1]} anos')'''
galera = []
dados = []
totma = totme = 0
for c in range(0, 4):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()
print(galera)
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de Idade.')
        totma += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totme += 1
print(f'Temos {totma} maiores e {totme} menores de idade')


