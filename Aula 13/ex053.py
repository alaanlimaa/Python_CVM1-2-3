frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
juntar = ''.join(palavras)
inverso = juntar[::-1]
if juntar == inverso:
    print(f'A frese/palavra {frase} ao inverso é {inverso}, PALÍNDROMO!')
else:
    print(f'A frese/palavra {frase} ao inverso é {inverso}, NÃO é PALÍNDROMO')
