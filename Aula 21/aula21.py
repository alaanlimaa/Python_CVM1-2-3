def contador(i, f, p):
    """
     - Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM! ')

#PARÂMETROS OPCIONAIS
def soma(a, b, c=0):
    s = a + b + c
    print(f'A soma é {s}')

#ESCOPO DE VARIÁVEIS:
def funcao(b):
    global n1
    n1 = 4
    b += 4
    c = 2
    print(f'N1 dentro vale {n1}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


n1 = 2
funcao(n1)
print(f'N1 fora vale {n1}')