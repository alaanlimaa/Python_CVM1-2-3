'''Desenvolva um programa que leia seis números inteiros e mostre a soma
apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.'''

#RESOLUÇÃO ALAN + PROFESSOR - consegui resolver sozinho apenas aprimorei o programa com o prof.
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}º número: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} número(s) PARE(S) e a soma do(s) mesmo(s) foi de {}!!!'.format(cont, soma))



