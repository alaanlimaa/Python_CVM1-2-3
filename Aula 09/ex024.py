'''Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.'''

cid = str(input('Escreva o nome de uma cidade: ')).strip()
print(cid[:5].upper() == 'SANTO')

'''Obs : strip foi usado para remover os espaços excedentes do lado esquerdo e do lado direito
assim caso o usuário digite com espaços antes do inicio da escreve, o programa ira ignorar,
usa-se upper, pois caso o usuário digite com alguma letra maiuscula o programa reconhece tbm.'''