galera = []
pessoas = []
maior = menor = 0
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))
    if len(galera) == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]
    galera.append(pessoas[:])
    pessoas.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=-' * 20)
print(f'Foram cadastradas {len(galera)} pessoas!')
print(f'O maior peso foi de {maior:.2f}Kg! ', end='')
maiorespesos = []
for p in galera:
    if p[1] == maior:
        print(f'[{p[0]}]  ', end='')
print()
print(f'O menor peso foi de {menor:.2f}Kg! ', end=' ')
for p in galera:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')

