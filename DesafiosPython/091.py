# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)}
ranking = []
print('-='*10)
print(' Valores Sorteados:')
print('-='*10)
for k,v in jogo.items():
    print(f'{k} tirou {v} no dado da sorte!')
    sleep(1)
print('-='*17)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) # Se for (0), mostra em orde chave; (1) mostra ordem randint, de acordo com o exercício
print(' == RANKING DOS JOGADORES ==')
print('-='*17)
for i, j in enumerate(ranking):
    print(f'    {i+1}º Lugar: {j[0]} com {j[1]} pontos !')
    sleep(1)