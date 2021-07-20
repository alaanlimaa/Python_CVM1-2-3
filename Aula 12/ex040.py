p1 = float(input('Nota P1:' ))
p2 = float(input('Nota P2: '))
media = (p1 + p2) / 2
if media < 5.0:
    print(f'Sua média foi {media:.2f}, \033[1;31mREPROVADO!\033[m')
elif media >= 5.0 and media < 7:
    print(f'Sua média foi {media:.2f}, \033[1;33mRECUPERAÇÃO!\033[m')
elif media >= 7.0:
    print(f'Sua média foi {media:.2f}, \033[1;32mAPROVADO!\033[m')
