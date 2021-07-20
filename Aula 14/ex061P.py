primeiro = int(input('Primeiro termo:'))
razao = int(input('Razão:'))
termo = primeiro # neste caso esta dizendo que a var vai começar com...
cont = 1 # a contagem vai começar em 1
while cont <= 10:
    print('{} → '. format(termo), end='')
    termo += razao
    cont += 1
print('FIM')
