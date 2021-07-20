'''Desenvolva um programa que leia o comprimento
de três retas e diga ao usuário se elas podem ou não formar um triângulo.'''

print('-=-' * 10)
print('   ANALISANDO UM TRIÂNGULO')
print('-=-' * 10)
r1 = float(input('Comprimento da PRIMEIRA reta: '))
r2 = float(input('Comprimento da SEGUNDA reta: '))
r3 = float(input('Comprimento da TERCEIRA reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')





