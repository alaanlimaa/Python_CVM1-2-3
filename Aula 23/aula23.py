try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('\033[1;033mTivemos um problema com o tipo de dados que você digitou! ☻\033[m')
except ZeroDivisionError:
    print('\033[1;32mNão é possível dividir um número por zero\033[m')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')
