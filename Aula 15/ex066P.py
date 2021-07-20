#FEITO POR MIM OKOKOKOKOKOOKOKOK

soma = cont = 0
while True:
    n = int(input('Digite um valor [999 STOP]: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Foram digitados {cont} números')
print(f'A soma entre eles é {soma}')
print('-=-' * 10)
print('PROGRAMA FINALIZADO...')