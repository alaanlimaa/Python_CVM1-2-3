primeiro = int(input('Primeiro termo:'))
razao = int(input('Razão da PA:'))
termo = primeiro  #neste caso esta dizendo que a var vai começar com...
cont = 1  #a contagem vai começar em 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} → '. format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Total de termos monstrados = {},  FIM!!!'.format(total))
