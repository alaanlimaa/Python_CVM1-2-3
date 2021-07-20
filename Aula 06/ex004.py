'''Faça um programa que leia algo pelo teclado
e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.'''

a = input('Digite algo: ')
print('O tipo primitivo é ')
print('É alphanumerico? ', a.isalnum())
print('É alphabético? ', a.isalpha())
print('É numérico? ', a.isnumeric())
print('São digitos ou digitado? ', a.isdigit())
print('Só tem letra minuscula? ', a.islower())
print('Só tem letra maiúscula? ', a.isupper())
print('Só tem espaços? ', a.isspace())
print('Está capitalizado? ', a.istitle())



