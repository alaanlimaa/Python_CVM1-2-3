numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
           'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
           'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze',
           'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
           'Dezenove', 'Vinte')
opcao = ''
while True:
    opcao = int(input('Digite um número entre 0 e 20: '))
    while opcao not in range(0, len(numeros)):
        print('Tente novamente, ', end='')
        opcao = int(input('Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {numeros[opcao]}')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:=^30}'.format('PROGRAMA FINALIZADO'))


