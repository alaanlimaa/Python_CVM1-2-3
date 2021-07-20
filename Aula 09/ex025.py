'''Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.'''

nome = str(input('Digite o nome completo de um pessoa qualquer: ')).strip()
print('O nome digitado tem silva? {}'.format('SILVA' in nome.upper()))

''' in" é um operador do python, nesse caso como estou colocanto uppr (tudo maiusculo) o que ele 
vai encontrar tbm tem que ser em maiusculo, mesma coisa serve para minusculo --- SILVA'''