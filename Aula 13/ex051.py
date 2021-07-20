#TREINAR

first = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = first + (10) * razao #CALCULO MATEMÁTICO PARA O 10º, 20º TERMO, ASSIM POR DIANTE
for c in range(first, decimo, razao):
    print(' {} '.format(c), end='→ ')
print('ACABOU!')