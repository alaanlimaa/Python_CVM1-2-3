'''Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:'''

p1 = float(input('Nota da P1: '))
p2 = float(input('Nota da P2: '))
media = (p1 + p2) / 2
if media < 5.0:
    print('Sua média foi {:.1f}, REPROVADO!'.format(media))
elif media >= 5.0 and media <= 6.9:
    print('Sua média foi {:.1f}, RECUPERAÇÃO'.format(media))
elif media >= 7.0:
    print('Sua média fou {:.1f}, APROVADO'.format(media))
