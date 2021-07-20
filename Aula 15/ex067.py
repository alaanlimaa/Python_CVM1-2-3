while True:
    num = int(input('Digite um número para ver sua tabuada: '))
    if num < 0:
        break
    for n in range(1, 11):
        print(f'{n} x {num} = {n * num}')
    print('=-=' * 20)
print('PROGRAMA FINALIZADO.')



