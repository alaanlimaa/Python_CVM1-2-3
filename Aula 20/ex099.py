def maior(* num):
    print('=' * 30)
    print('Analisando os respectivos valores . . . ')
    cont = maior = 0
    for n in num:
        print(f'{n} ', end='')
        if cont == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        cont += 1
    print(f' Foram digitados {cont} valores ao todo.')
    print(f'O maior valor foi {maior}.')


maior(4, 8, 9, 2, 1, 6)
maior(5, 1, 6)
maior(4, 2)
maior()
