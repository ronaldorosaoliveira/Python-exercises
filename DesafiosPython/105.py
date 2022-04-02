# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# – Quantidade de notas # – A maior nota # – A menor nota # – A média da turma # – A situação (opcional)
# Adicione também as docstrings

def notas(*n, sit=False):
    """
    -> Função para analisar notas e situação de vários alunos
    :param n: uma ou mnais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionários com várias informações sobre a situação da turma
    """
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 6:
            r['situação'] = 'Boa'
        elif r['média'] <= 4:
            r['situação'] = 'Ruim'
        else:
            r['situação'] = 'Razoável'
    return r

resp = notas(2, 2, 5, sit=True)
print(resp)
#help(notas)