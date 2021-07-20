def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO: por favor , digite um número inteiro válido\033[m')
            continue
        else:
            return n

def leiaReal(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO: por favor , digite um número inteiro válido\033[m')
            continue
        else:
            return n



n = leiaInt('Digite um número Inteiro: ')
nr = leiaReal('Digite um número Real:')
print(f'Você acabou de digitar os números:\n Inteiro: {n} \n Real: {nr}')