from time import sleep
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 30)
    print(f'Contagem de {i} até {f} de {p} em {p}!')
    sleep(0.2)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.2)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.2)
            cont -= p
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de persol=nalizar a contagem')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
passo = int(input('Passo:  '))
contador(ini, fim, passo)