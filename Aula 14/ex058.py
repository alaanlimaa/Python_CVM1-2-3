from random import randint
from time import sleep
cpu = randint(0, 10)
print('QUAL NÚMERO PENSEI!!')
print('-=-' * 15)
sleep(2)
acertou = False
tentativas = 0
while not acertou:
    jogador = int(input('Digite um numero entre 0 e 10: '))
    tentativas += 1
    if jogador == cpu:
        acertou = True
    if jogador > cpu:
        print('POUCO MENOS...')
    if jogador < cpu:
        print('POUCO MAIS ...')
print(f'Você tentou {tentativas} palpites, a cpu pensou em {cpu}. OBRIGADO')