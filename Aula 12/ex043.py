from time import sleep
peso = float(input('Peso da pessoa (Kg): '))
altura = float(input('Altura da pessoa (m): '))
imc = peso / (altura * altura)
print('CALCULANDO. . .')
sleep(3)
print('Seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso!')
elif imc < 25:
    print('Peso ideal!')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida, cuidado! ')


