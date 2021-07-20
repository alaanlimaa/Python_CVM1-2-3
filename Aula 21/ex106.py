from time import sleep
c =('\33[m',        # 0 → SEM COR
    '\33[0;41m',    # 1 → VERMELHO
    '\33[0;42m',    # 2 → VERDE
    '\33[0;43m',    # 3 → AMARELO
    '\33[0;44m',    # 4 → AZUL
    '\33[0;45m',    # 5 → ROCHO
    '\33[7;40m'     # 6 → AZUL-CLARO
    )

def ajuda(com):
    título(f'ACESSANDO O MANUAL DO COMANDO \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)

def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}  ')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca → ')).strip().lower()
    if comando.upper() == 'FIM':
        título('ATÉ LOGO!', 1)
        break
    else:
        ajuda(comando)

