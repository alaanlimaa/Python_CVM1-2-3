nome = str(input('Qual é o seu nome?')).strip().upper()
if nome == 'ALAN':
    print('Que nome bonito!!')
elif nome == 'MARIA' or nome == 'LEVI' or nome == 'ALINE':
    print('Seu nome é bem popular no Brasil!!!')
elif nome in 'ANA CLAUDIA JESSICA JULIANA':
    print('Um belo nome feminino!')
else:
    print('Seu nome é bem normal!')
print('Tenha uma ótima noite {} !!'.format(nome.title()))
