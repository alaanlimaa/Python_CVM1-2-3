resp = 'Ss'
cont = soma = maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um valor: '))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
    resp = str(input('Deseja continuar [S/N] ')).strip().upper()[0]
print(f'Foram digitados {cont} valores e a média entre eles é {soma / cont:.2f}!')
print(f'O maior é {maior} e o menor é {menor}!')





