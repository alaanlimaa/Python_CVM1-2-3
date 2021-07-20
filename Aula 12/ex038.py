n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
if n1 > n2:
    print(f'Entre {n1} e {n2} o maior é {n1}')
elif n1 < n2:
    print(f'Entre {n1} e {n2} o maior é {n2}')
else:
    print(f'Entre {n1} e {n2}, os dois são iguais!')