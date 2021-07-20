from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''QUAL OPÇÃO DESEJA:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos número
    [ 5 ] sair do programa''')
    opcao = int(input('Qual opcao desejada? '))
    if opcao == 1:
        print(f'O resultado da soma entre {n1} e {n2} = {n1 + n2}')
    elif opcao == 2:
        print(f'O resultado do produto entre {n1} e {n2} = {n1 * n2}')
    elif opcao == 3:
        if n1 > n2:
            print(f'O maior entre {n1} e {n2} é o {n1}')
        else:
            print(f'O maior entre {n1} e {n2} é o {n2}')
    if opcao == 4:
        print('Digite novos números!!')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    if opcao == 5:
        print('Finalizando programa.....')
    print('-=-' * 20)
sleep(2)
print('PROGRAMA FINALIZADO... OBRIGADO!!!')


