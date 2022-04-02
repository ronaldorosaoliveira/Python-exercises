# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

lista = ('Corinthians', 'Palmares', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético-MG', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport-RE', 'Vitória-BA', 'Coritiba', 'Ponte Preta', 'Atlético-GO')
print(f'Os 5 primeiros colocados são: {lista[0:5]}')
print(f'\nOs últimos 4 colocados são: {lista[-4:]}')
print(f'\nOs times em ordem alfabética são: {sorted(lista)}')
print(f'\nO Time Chapecoense está na {lista.index("Chapecoense")+1}ª posição')