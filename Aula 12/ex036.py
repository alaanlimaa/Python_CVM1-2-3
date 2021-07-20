valor = float(input('Qual valor da casa? R$ '))
salario = float(input('Qual seu salário? R$ '))
anos = int(input('Em quantos anos pretende pagar? '))
prestacao = valor / (30 * 12)
minimo = salario * 0.3
percentual = (prestacao / salario) * 100
if prestacao <= minimo:
    print(f'A prestação será de R$ {prestacao:.2f}\nConsumirá {percentual:.2f}% do seu capital mensal.')
    print('Empréstimo APROVADO!!')
else:
    print(f'A prestação será de R$ {prestacao:.2f}\nConsumirá {percentual:.2f}% do seu capital mensal.')
    print('Emprestimo NEGADO!!')




