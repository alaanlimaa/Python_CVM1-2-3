boletim = []
while True:
    nome = str(input('Nome: ')).title()
    m1 = float(input('Nota M1: '))
    m2 = float(input('Nota M2: '))
    media = (m1 + m2) / 2
    if media >= 5:
        boletim.append([nome, [m1, m2], media, 'Aprovado'])
    else:
        boletim.append([nome, [m1, m2], media, 'Reprovado'])
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(boletim)
print('=' * 40)
print(f'{"No.":<4}{"NOME":<6}{"MÉDIA":>10}{"STATUS":>15}')
for a, l in enumerate(boletim):
    print(f'{a:<4}{l[0]:<6}{l[2]:>9}{l[3]:>16}')
print('=' * 40)
while True:
    opc = int(input('Deseja monstrar as notas de qual aluno? (Digite o nº) [999 to break] '))
    if opc == 999:
        break
    print(f'As notas do aluno {boletim[opc][0]} são {boletim[opc][1]}, {boletim[opc][3]}')
print('PROGRAMA FINALIZADO')





