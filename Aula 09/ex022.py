'''Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas e minúsculas. OKAY
Quantas letras ao todo (sem considerar espaços).
Quantas letras tem o primeiro nome.'''

name = str(input('Digite seu nome completo: ')).strip()
print('Seu nome com letras maiúsculas = {} '.format(name.upper()))
print('Seu nome com letras minúsculas = {}'.format(name.lower()))
print('Seu nome contém um total de {} letras (sem os espaços)'.format(len(name)-name.count(' ')))
separar = name.split()
print('Seu primeiro nome é {} e contém {} letras'.format(separar[0], len(separar[0])))
