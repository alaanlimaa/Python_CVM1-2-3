'''for c in range(1, 10): #usar este comando apenas quando vc sabe o limite, ponto final, caso não saiba usa-se while
    print(c)
print('FIM')'''

# USANDO WHILE, bom usar quando não sabemos o limite final do loob, ou seja, até que ponto chegar
'''c = 1  #COMEÇA NO 1
while c < 10: #ENQUANTO FOR MENOR QUE 10, CONTINUE COM OS PASSOS
    print(c)
    c += 1 #OU TBM PODEMOS USAR C = C + 1, essa matemática é usada, pois sempre que acabar um loop ele vai somar mais 1 passo até 10
print('FIM')'''

# EXEMPLO DE USO DO WHILE QUANDO VC NÃO SABE O LIMITE FINAL DA OPERAÇÃO
r = 'S'   #ACONTAGEM SE INICIA EM 1, ou str que deseja finalizar o programa
while r == 'S': #O programa será paralisado apenas quando o usuário digitar o zero ou a letra, neste caso, condição de parada
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] : ')).upper()
print('FIM')

