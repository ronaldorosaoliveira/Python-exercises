# Crie um programa que leia o ano de nascimento de sete pesoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
anoatual = date.today().year
totalmaior = 0
totalmenor = 0
for c in range(1, 8):
    nascimento = int(input(f'Em que ano a {c}ª pessoa nasceu ? '))
    idade = anoatual - nascimento
    if idade >= 18:
        totalmaior += 1
    else:
        totalmenor += 1
print(f'\nAo todo tivemos \033[34m{totalmaior}\033[m pessoa(s) com a maioridade atingida e \033[34m{totalmenor}\033[m pessoa(s) que ainda não atingiram a maioridade.')