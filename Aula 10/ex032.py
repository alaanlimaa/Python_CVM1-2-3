'''Faça um programa que leia um ano qualquer e mostre se ele é bissexto.'''

# FORMA MATEMÁTICA DE RESOLVER
'''ano = int(input('Qual ano deseja análisar? '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:     # != DIFERENTE
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))'''

# FORMA AUTOMATICA DO COMPUTADOR
from datetime import date
ano = int(input('Qual ano deseja análisar? Coloque 0 para analisar o ano atutal: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:     # != DIFERENTE
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))