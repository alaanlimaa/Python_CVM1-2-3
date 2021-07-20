'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.'''

# DESENVOLVIDO POR MIM MESMO
'''velocidade = int(input(' Qual a velocidade em Km/h que o carro estava: '))
if velocidade > 80:
    print('Você foi multado')
    print('O valor da multa é R$ 7,00 km acima do limite')
    print('Valor a ser pago é de R$ {:.2f} '.format((velocidade-80)*7))
else:
    print('Siga em frente')'''

# DESENVOLVIDO PELO PROFESSOR
velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu a velocidade permitida de 80 Km/h')
    multa = (velocidade - 80) * 7
    print(' Você deve pagar uma multa no valor de R$ {:.2f} !'.format(multa))
print('Ótimo dia senhor, dirija com segurança!!!')

