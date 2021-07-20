maior18 = conth = contf = Fmenor20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo [F/M]: ')).strip().upper()[0]
    if idade > 18:
        maior18 += 1
    if sexo == 'M':
        conth += 1
    if sexo == 'F' and idade < 20:
        Fmenor20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    print('-=-' * 15)
    if resp == 'N':
        break
print(f'São {maior18} pessoas maiores de 18 anos')
print(f'Foram cadastrados {conth} homens')
print(f'Foram cadastradas {Fmenor20} mulheres com menos de 20 anos! ')

