aluno = {}
aluno['Nome'] = str(input('Nome aluno: ')).strip().title()
aluno['Média'] = float(input(f'Média do(e) {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Status'] = 'APROVADO'
elif aluno['Média'] >= 5 < 7:
    aluno['Status'] = 'EM RECUPERAÇÃO'
else:
    aluno['Status'] = 'REPROVADO'
for i, d in aluno.items():
    print(f'    -{i} é igual a {d}')
    