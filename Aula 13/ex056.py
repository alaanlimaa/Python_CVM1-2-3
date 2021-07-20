midade = Hmaior = nomevelho = contM20 = 0
for p in range(1, 5):
    print('-=-' * 10)
    print(f'{p}º pessoa ')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).strip()[0]
    midade += idade
    if p == 1 and sexo in 'Mm':
        Hmaior = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > Hmaior:
        Hmaior = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        contM20 += 1
print(f'A média de idade do grupo é {midade / p:.2f} anos')
print(f'O homem mais velho tem {Hmaior} anos eo seu nome é {nomevelho}')
print(f'São {contM20} mulheres menores de 20 anos')
