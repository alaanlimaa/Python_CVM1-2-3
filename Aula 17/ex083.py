expr = str(input('Escreva uma expressão: '))
cont = []
for simb in expr:
    if simb == '(':
        cont.append('(')
    elif simb == ')':
        if len(cont) > 0:
            cont.pop()
        else:
            cont.append(')')
            break
if len(cont) == 0:
    print('Sua expressão está VÁLIDA')
else:
    print('Sua expressão está INVÁLIDA')