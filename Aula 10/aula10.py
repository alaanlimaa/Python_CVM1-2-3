# EXEMPLO 1 = TEMPO DE VIDA DO SEU CARRO
'''time =int(input('Quantos anos tem seu carro: '))
if time <=3:
    print('Seu carro é zero bala ainda')
else:
    print('Carro velho em')
print('=== FIM ===')'''

# USANDO CONDIÇÃO SIMPLIFICADA PARA REDUZIR O Nº DE LINHAS

'''time =int(input('Quantos anos tem seu carro ?'))
print('Carro novo' if time <=3 else 'Carro velho')
print(' == FIM == ')'''

# EXEMPLO 2
'''name = str(input('Qual é o seu nome? ')).strip().capitalize()
if name == 'Alan':
    print('Que nome lindo brother')
else:
    print('Não é tão bonito')
print('Bom dia, {}'.format(name))'''

# EXEMPLO 3
n1 = float(input('Qual a nota da primeira prova: '))
n2 = float(input('Qual a nota da segunda prona: '))
m = (n1 + n2)/2
print('Sua média foi {:.1f}'.format(m))
if m >= 5:
    print('Você foi aprovado, parabéns')
else:
    print('Você foi reprovado, tente novamente')




