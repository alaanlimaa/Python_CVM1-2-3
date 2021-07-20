n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))
n4 = int(input('Quarto número: '))
numeros = (n1, n2, n3, n4)
print(f'Você digitou os números {numeros}')
print(f'O número 9 apareceu {numeros.count(9)} vezes!')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3)+1}ª posição!')
else:
    print('O número 3 não foi digitado!')
cont = 0
print(f'Os valores pares digitados foram :', end=' ')
for n in numeros:
    if n % 2 == 0:
        cont += 1
        print(n, end=' ')
print(f'\nUm total de {cont} números pares')

