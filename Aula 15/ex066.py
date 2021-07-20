soma = cont = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    soma += num
    cont += 1
print('PROGRAMA FINALIZADO!')
print(f'Foram digitados {cont} números e soma entre ele é {soma}')