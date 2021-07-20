'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços. Exemplos de palíndromos:'''

#FORMA 1 DE RESOLUÇÃO
'''frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
juntar = ''.join(palavras)
inverso = ''
for letra in range(len(juntar) -1, -1, -1):
    inverso += juntar[letra]
print('O inverso de {} é {}'.format(juntar, inverso))
if inverso == juntar:
    print('Temos um palímdromo ')
else:
    print('Não temos um palindromo')'''

#FORMA 2 DE RESOLUÇÃO SEM O FOR, PORÉM COM FATIAMENTO.
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
juntar = ''.join(palavras)
inverso = juntar[::-1]
print('O inverso de {} é {}'.format(juntar, inverso))
if inverso == juntar:
    print('Temos um palímdromo ')
else:
    print('Não temos um palindromo')
