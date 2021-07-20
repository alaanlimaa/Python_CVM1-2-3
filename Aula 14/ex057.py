sexo = str(input('Sexo [F/M]: ')).strip().upper()[0]
while sexo not in 'FM':
    print('Digite novamente!!')
    print('-=-' * 15)
    sexo = str(input('Sexo [F/M]: ')).strip().upper()[0]
print('===== PROGRAMA FINALIZADO =====')
