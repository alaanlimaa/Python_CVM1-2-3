primeiro = int(input('Termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} →', end='')
        termo += razao
        cont += 1
    print(' PAUSA...')
    mais = int(input('Deseja que monstre mais, quantos? [0 STOP]'))
print('FIM...')
print(total)




