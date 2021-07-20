n = int(input('Digite um valor: '))
cont = soma = 0
while n != 999:
    soma += n
    n = int(input('Digite um valor: '))
    cont += 1
print(f'Foram digitados {cont} e a soma entre eles é {soma}')

#PROFESSOR
n = cont = soma = 0
n = int(input('Digite um valor [999 stop!]: '))
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um valor [999 stop!]: '))
print('Você digitou {} número e a soma entre eles foi de {}'.format(cont, soma))
print('FINALIZANDO PROGRAMA...')
