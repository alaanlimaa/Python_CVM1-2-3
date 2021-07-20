'''Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
e R$0,45 parta viagens mais longas.'''

# MINHA RESOLUÇÃO
'''from time import sleep
dist = float(input('Qual a distância em km percorrida na viagem? '))
print('Para viagens até 200Km será cobrado R$ 0,50 por Km e R$ 0,45 para viagens mais longas')
print('Você esta prestes a começar uma viagem de {} Km'.format(dist))
print('PROCESSANDO...')
sleep(3)
if dist <= 200:
    print('O valor a ser pago é de R$ {:.2f} '.format(dist * 0.50))
else:
    print(' O valor a ser pago é de R$ {:.2f}'.format(dist * 0.45))'''

# RESOLUÇÃO PROFESSOR
dist = float(input('Qual é a distância da sua viagem? '))
print('Você esta prestes a começar uma viagem de {} Km'.format(dist))
preço = dist * 0.50 if dist <= 200 else dist * 0.45 #OUTRA FORMA DE USAR
print('E o preço da sua pssagem será de R$ {:.2f}'.format(preço))

