#RESOLUÇÃO ALAN
'''while True:
    print('=' * 20)
    tab = int(input('Quer ver a tabuada de qual valor? '))
    print('=' * 20)
    if tab < 0:
        break
    n = 1
    r = tab
    while n <= 10:
        print(f'{n} x {tab} = {r}')
        n += 1
        r = n * tab
print('PROGRAMA FINALIZADO')'''

#RESOLUÇÃO PROFESSOR
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('=' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{c} x {n} = {c * n}')
    print('=' * 30)
print('PROGRAMA FINALIZADO')






