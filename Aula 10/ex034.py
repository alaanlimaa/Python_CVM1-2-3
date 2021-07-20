'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu
 aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%.
 Para os inferiores ou iguais, o aumento é de 15%'''

# MINHA RESOLUÇÃO
sal = float(input('Qual seu salário? Digite o mesmo:'))
print('Para salários superiores a R$ 1250,00, aumento será de 10%. Para salários inferiores ou iguais'
      ', o aumento é de 15%')
if sal > 1250.00:
    print('AUMENTO DE 10%, novo salário será de R$ {:.2f} !'.format((sal * 0.10) + sal))
else:
    print('AUMENTO DE 15%, novo salário será de R$ {:.2f}'.format((sal * 0.15) + sal))
