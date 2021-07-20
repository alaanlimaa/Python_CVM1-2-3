from random import randint
computador = randint(0, 10)
print('Sou seu computador... \nAcabei de pensar em um número de 0 à 10')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente outra vez!!!')
        elif jogador > computador:
            print('Menos... Tente outra vez!!!')
print('Acertou com {} palpites. Parabéns'.format(palpites))
