def notas(*n, sit=False):
    '''
    :param n: Notas dos alunos
    :param sit: Se deseja que mostre a  situação = True se não False
    :return: Dicionário com várias informações com a situação da turma
    '''
    r = {}
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n)/len(n)
    if sit: #Mesma coisa que  'if sit == True:'
        if r['Média'] >= 7:
            r['Situação'] = 'BOA'
        elif r['Média'] >= 5:
            r['Situação'] = 'RAZOÁVEL'
        else:
            r['Situação'] = 'RUIM'
    return r


resp = notas(5.3, 2.5, 10, sit=True)
print(resp)





