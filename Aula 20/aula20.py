'''def soma(a, b):
    a = int(input('Digite o valor de A: '))
    b = int(input('Digite o valor de B: '))
    s = a + b
    print(f'{a} + {b} = {s}')
    print('-' * 15)


# Programa principal
soma(a='', b='')
soma(a='', b='')'''

'''def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números!')


contador(2, 4, 7)'''
def dobra(list):
    pos = 0
    while pos < len(list):
        list[pos] *= 2
        pos += 1


valores = [7, 4, 6, 9]
dobra(valores)
print(valores)
