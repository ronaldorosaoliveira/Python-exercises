# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar no serviço militar
# Se é hora dele se alistar
# Se já passou do tempo de alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
from datetime import date
ano = int(input('Digite o ano em que você nasceu: '))
atual = date.today().year
idade = atual - ano
print(f'Quem nasceu em {ano} completará {idade} anos em {atual} !')
print(f'Você já se alistou ou deveira se alistar há {idade - 18} anos !')
print(f'O ano do seu alistamento foi em {ano + 18} !')
