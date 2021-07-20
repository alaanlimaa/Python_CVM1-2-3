from datetime import date
atual = date.today().year
somamenor = somamaior = 0
for pessoas in range(1, 8):
    ano = int(input('Ano de nascimento: '))
    idade = atual - ano
    if idade < 18:
        somamenor += 1
    else:
        somamaior += 1
print(f'São {somamenor} pessoas MENORES de idade!!')
print(f'São {somamaior} pessoas MAIORES de idade')


