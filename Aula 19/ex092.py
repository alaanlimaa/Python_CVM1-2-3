from datetime import date
dados = {}
dados['Nome'] = str(input('Nome: ')).strip().title()
nasc = int(input('Ano de nascimento :'))
dados['Idade'] = date.today().year - nasc
resp = ' '
while resp not in 'SN':
    resp = str(input('Contém CTPS [S/N]? ')).strip().upper()[0]
    if resp == 'S':
        dados['CTPS'] = int(input('Digite o número de sua CTPS: '))
        dados['Salário'] = float(input('Salário: R$ '))
        dados['Contratação'] = int(input('Ano de contratação: '))
        exp = date.today().year - dados['Contratação']
        aposentadoria = int((exp + dados['Idade']) + (0.40 * 65))
        dados['Aposentadoria'] = aposentadoria
    if resp == 'N':
        dados['CTPS'] = 'Não possui CTPS'
print(dados)
print('=' * 30)
for k, v in dados.items():
    if k == 'Salário':
        print(f'{k} = R$ {v:.2f}')
    elif k == 'Aposentadoria':
        print(f'{k} com {v} anos')
    else:
        print(f'{k} = {v}')
print()
print('PROGRAMA FINALIZADO')
