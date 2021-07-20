from time import sleep
dados = {}
dados['Nome'] = str(input('Nome aluno: ')).strip().title()
dados['Média'] = float(input(f'Média do(e) {dados["Nome"]}: '))
print('=' * 40)
sleep(2)
for i, d in dados.items():
    print(f'    -{i} é igual a {d}')
    sleep(1)
if dados['Média'] >= 7:
    dados['Status'] = 'APROVADO'
elif dados['Média'] >= 5 < 7:
    dados['Status'] = 'EM RECUPERAÇÃO'
else:
    dados['Status'] = 'REPROVADO'
sleep(1)
print(f'    -A situação é !!!{dados["Status"]}!!!')




