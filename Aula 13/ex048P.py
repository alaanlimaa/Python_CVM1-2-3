'''Faça um programa que calcule a soma entre todos os números impares que
são múltiplos de três e que se encontram no intervalo de 1 até 500.'''

soma = 0
cont = 0
for num in range(1, 501, 2): #assim ele conta apenas os número ímpares
    if num % 3 == 0:
        cont = cont + 1
        soma = soma + num
print('A soma entre os {} valores é de {}!'.format(cont, soma))