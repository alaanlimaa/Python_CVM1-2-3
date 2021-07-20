num = (int(input('Primeiro número: ')),
       int(input('Segundo número: ')),
       int(input('Terceiro número: ')),
       int(input('Quarto número: ')))
print(f'Você digitou os valores {num}!')
print(f'O número 9 apareceu {num.count(9)} vezes!')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posição!')
else:
    print('O número 3 não foi digitado!')
print('Os números pares foram', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')

