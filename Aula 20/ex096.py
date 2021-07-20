def titulo(txt):
    print()
    print(txt)
    print('-' * 30)

def area(a, b):
    a = float(input('Lagura terreno [m²]: '))
    b = float(input('Comprimento terreno [m²]: '))
    t = a * b
    print(f'A área de um terreno de {a}x{b} tem {t} m²')


titulo('    CONTROLE DE TERRENOS    ')
area(a='', b='')
