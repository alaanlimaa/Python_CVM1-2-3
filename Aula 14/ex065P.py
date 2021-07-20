resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Deseja continuar [S/N]:')).strip().upper()[0]
media = soma / quant
print('Foram digitados {} números e a média entre eles é de {}'.format(quant, media))
print('O maior valor é {} e p menor foi {}'.format(maior, menor))
