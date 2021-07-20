pessoas = []
geral = []
maior = menor = 0
while True:
    pessoas.append(str(input('Nome: ')).title())
    pessoas.append(float(input('Peso: ')))
    if len(geral) == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]
    geral.append(pessoas[:])
    pessoas.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('=' * 40)
print(geral)
print(f'Foram cadastradas {len(geral)} pessoas')
print(f'O MAIOR peso foi {maior}Kg, nomes: ', end='')
for p in geral:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O MENOR peso foi {menor}Kg, nomes: ', end='')
for p in geral:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
print()
print('=' * 40)
print('PROGRAMA FINALIZADO.')

