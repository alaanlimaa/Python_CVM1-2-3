pessoas = {'nome': 'Alan', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]}')
print(pessoas.values())
print(pessoas.keys())
print(pessoas.items())
from time import sleep
for k, p in pessoas.items():
    print(f'O {k} é {p}!!')
    sleep(1)
print('FIM DO PROGRAMA')


