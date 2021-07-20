tot18 = toth = totm20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo [F/M]: ')).upper().strip()[0]
    if idade > 18:
        tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade < 20:
        totm20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        print('-=' * 20)
    if resp == 'N':
        break
print(f'{tot18} pessoas são maiores de 18 anos')
print(f'Foram cadastrados {toth} homens ao todo!')
print(f'Temos {totm20} mulheres menores de 20 anos ')
print('PROGRAMA FINALIZADO')
