def voto(b):
    from datetime import date
    idade = date.today().year - b
    if idade < 16:
        return f'Você tem {idade} anos, voto NEGADO'
    elif idade < 18:
        return f'Você tem {idade} anos, voto é OPCIONAL'
    elif idade >= 18 and idade <= 70:
        return f'Você tem {idade} anos, voto é OBRIGATÓRIO'
    else:
        return f'Você tem {idade} anos, voto NEGADO'


#Programa principal
while True:
    ano = int(input('Ano de nascimento: '))
    print(voto(ano))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 15)
print('PROGRAMA FINALIZADO')
