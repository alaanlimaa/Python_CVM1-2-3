print('{:=^40}'.format('LOJAS ALAN LIMA')) #OBSERVAR O STYLO
valor = float(input('Valor toal dos produtos: R$ '))
print('''Opções de pagamento :
[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista no cartão
[ 3 ] Em até 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual opção desejada? '))
if opcao == 1:
    pgto = valor - (valor * 0.1)
    print('Desconto de 10%, valor a ser pago é R$ {:.2f}'.format(pgto))
elif opcao == 2:
    pgto = valor - (valor * 0.05)
    print('Desconto de 5%, valor a ser pago é R$ {:.2f}'.format(pgto))
elif opcao == 3:
    print('Preço normal, R$ {:.2f} parcelado em 2x de R$ {:.2f} !'.format(valor, valor / 2))
elif opcao == 4:
    pgto = valor + (valor * 0.20)
    print('Juros de 20%, valor a ser pago é de R$ {}'.format(pgto))
    parcelas = int(input('Quantas parcelas deseja? '))
    print('Será pago em {:.0f}x de R$ {:.2f}'.format(parcelas, pgto / parcelas))
else:
    print('OPÇÃO INEXISTENTE')
