from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
atual = date.today().year
idade = atual - ano
if idade < 18:
    print(f'Você tem {idade} anos e falta {18 - idade} anos para seu alistamento')
elif idade == 18:
    print(f'VocÊ tem {idade} anos')
else:
    print(f'Você tem {idade} anos, seua alistamento foi à {idade - 18} anos atraz')

