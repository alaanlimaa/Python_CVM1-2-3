km = float(input('Quantos Km você percorreu com o carro: '))
dias = int(input('Quantos dias ficou com o carro: '))
al = (dias*60) + (km*0.15)
print('O total do aluguel é R${:.2f}'.format(al))
