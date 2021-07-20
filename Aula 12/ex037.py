num = int(input('Digite um número inteiro: '))
print('-=-' * 10)
print('''ESCOLHA AS OPÇÕES ABAIXO: 
[ 1 ] binário
[ 2 ] octal
[ 3 ] hexadecima''')
print('-=-' * 10)
opcao = int(input('Qual opção desejada? '))
if opcao == 1:
    print(f'Seu número transformado em BINÁRIO é:\n{bin(num)[2:]}!!')
elif opcao == 2:
    print(f'Seu número transformado em OCTAL é:\n{oct(num)[2:]}')
elif opcao == 3:
    print(f'Seu número transformado em HEXADECIMAL é:\n{hex(num)[2:]}')
else:
    print('OPÇÃO INVÁLIDA!!!')



