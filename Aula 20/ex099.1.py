# RESOLUÇÃO UTILIZANDO LISTA (ERA PARA USAR PARÂMETROS)
def maior(*num):
    print('=' * 40)
    print('Analisando os valores passados...')
    lista = (num)
    if len(lista) == 0:
        print(f'Foram informados 0 valores ao todo!')
        print(f'O maior valor informado foi 0')
    else:
        for c in lista:
            print(f'{c} ', end='')
        print(f' - Foram informados {len(lista)} valores ao todo!')
        print(f'O maior valor informado foi {max(lista)}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()