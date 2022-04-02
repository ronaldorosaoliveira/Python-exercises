# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
# Chama-se ano bissexto o ano ao qual é acrescentado um dia extra, ficando com 366 dias, ocorrendo a cada quatro anos (exceto anos múltiplos de 100 que não são múltiplos de 400).

from datetime import date
ano = int(input('Qual o ano a ser analisado ? Se for o ano atual, digite 0 : '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é Bissexto')
else:
    print(f'O ano {ano} não é Bissexto')
