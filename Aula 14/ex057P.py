'''sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    print('=-' * 20)
    sexo = str(input('Dado inválido, digite novamento seu sexo [M/F] :')).strip().upper()[0]
print('=-' * 20)
if sexo == 'F':
    print('Seu sexo é Feminino, obrigado!!!')
elif sexo == 'M':
    print('Seu sexo é Masculino, Obrigado !!!')'''

#RESOLUÇÃO ALAN
sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    print('Inválido digite novamento!!')
    print('-=-' * 20)
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
if sexo == 'M':
    print('Seu sexo é {}asculino!'.format(sexo))
if sexo == 'F':
    print('Seu sexo é {}eminino!!!'.format(sexo))
print('OBRIGADO!!!')










