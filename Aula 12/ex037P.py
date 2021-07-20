'''Escreva um programa em Python que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão: 1 para binário,
2 para octal e 3 para hexadecimal.'''

#RESOLUÇÃO ALAN + PROFESSOR
num = int(input('Digite um número interiro: '))
print('''Escolha uma das opções abaixo:
[ 1 ] converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
opcao = int(input("Sua opção: "))
if opcao == 1:
    print('{} convertido em BINÁRIO é igual a {} '.format(num, bin(num)[2:])) #usa-se [2:0] formatação do texto, não quero que apareça as duas primeiras letras
elif opcao == 2:
    print('{} convertido em OCTAL é igual a {} '.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido em HEXADECIMAL é igual a {} '.format(num, hex(num)[2:]))
else:
    print('Opção inválida!!!')
