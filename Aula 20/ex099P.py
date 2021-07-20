from time import sleep
def maior(* num):
    cont = maior = 0
    print('=' * 40)
    print('Analisando os valores passados... ')
    for n in num:
        print(f'{n} ', end='')
        sleep(0.4)
        if cont == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        cont += 1
    print(f' Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


maior(2, 9, 4, 5, 13, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()