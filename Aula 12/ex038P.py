'''Escreva um programa que leia dois números inteiros e compare-os.
mostrando na tela uma mensagem:'''

n1 = int(input('Escreva um número interiro: '))
n2 = int(input('Escreva outro número inteiro: '))
if n1 > n2:
    print('O primeiro é o MAIOR !')
elif n2 > n1:
    print('O segundo número é o MAIOR !')
else:
    print(' Não existe MAIOR, pois os dois são iguais')
