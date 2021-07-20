from time import sleep
n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Números
    [ 5 ] Sair do programa''')
    opcao = int(input("Qual é a sua opção: "))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} + {} = {}!'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n2 * n1
        print('O produto entre {} * {} = {}!'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre os números {} e {} o maior é {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe novamento os números!!')
        n1 = int(input('Primeiro Valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida, tente outro número!')
    print('-=-' * 20)
    sleep(2)
print('FIM DO PROGAMA')