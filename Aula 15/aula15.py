n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma dos números vale {s}') #Forma nova de escrever 3.6+
print('A soma dos números vale {}'.format(s)) #Forma utilizada no Python 3



