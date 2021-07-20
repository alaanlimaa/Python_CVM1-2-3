from random import randint
itens = ('Papel', 'Tesoura', 'Pedra')
computador = randint(0, 2)
print('''Escolha uma opção abaixo:
[ 0 ] Papel
[ 1 ] Tesoura
[ 2 ] Pedra''')
opcao = int(input('Qual opção deseja: '))
print(f'O computador jogou {itens[computador]}!')
print(f'Você jogou {itens[opcao]}')
if computador == 0:
    if opcao == 0:
        print('RODADA EMPATADA!')
    elif opcao == 1:
        print('JOGADOR VENCEU!!!')
    elif opcao == 2:
        print('COMPUTADOR VENCEU!!!')
elif computador == 1:
    if opcao == 0:
        print('COMPUTADOR VENCEU')
    elif opcao == 1:
        print('RODADA EMPATADA!!')
    elif opcao == 2:
        print('JOGADOR VENCEU!!')
elif computador == 2:
    if opcao == 0:
        print('JOGADOR VENCEU!')
    elif opcao == 1:
        print('COMPUTADOR VENDEU')
    elif opcao == 2:
        print('RODADA EMPATADA')
else:
    print('JOGADA INVÁLIDA!')