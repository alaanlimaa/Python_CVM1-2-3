'''Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date
atual = date.today().year #TIVE DIFICULDADE QUI
ano = int(input('Qual seu ano de nascimento? '))
sexo = str(input('Qual seu sexo, masculino ou feminino? ')).strip().upper()
idade = atual - ano
print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif sexo == 'FEMININO':
    print('Você não precisa se alistar')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para seu alistamento'.format(saldo))
    print('Seu alistamento será em {}'.format(atual + saldo))
else: #PODE-SE USAR TBM O ELIF > 18:
    saldo = idade - 18
    print('Você ja deveria ter se alistado a {} anos atrás'.format(saldo))
    print('Você se alistou no ano de {}'.format(atual - saldo))

