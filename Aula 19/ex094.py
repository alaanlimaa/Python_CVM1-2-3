pessoas = {}
geral = []
sidade = 0
while True:
    pessoas['nome'] = str(input('Nome: ')).title()
    pessoas['sexo'] = str(input('Sexo [M/F]:')).strip().upper()[0]
    pessoas['idade'] = int(input('Idade: '))
    sidade += pessoas['idade']
    resp = ' '
    geral.append(pessoas.copy())
    while resp not in 'SN':
        resp = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 40)
print(f'Foram cadastradas {len(geral)} pessoas!!')
media = sidade / len(geral)
print(f'A idade média é {media : .0f} anos')
mulheres = []
idadesup = []
for i, v in enumerate(geral):
    if geral[i]['sexo'] == 'F':
        mulheres.append(geral[i]["nome"])
    if geral[i]['idade'] > media:
        idadesup.append(geral[i]["nome"])
print(f'As mulheres cadastradas são: {mulheres}')
print(f'As pessoas com idades superiores a {media:.0f} anos são: {idadesup}')
