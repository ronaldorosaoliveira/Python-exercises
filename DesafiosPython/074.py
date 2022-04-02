# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

menor = maior = ' '
cont = 0

lista = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print('Os número sorteados foram', end=' ')
for n in lista:
    print(f'{n}', end=' ')
print(f'\n\nO maior valor sorteado foi {max(lista)}\n')
print(f'O menor valor sorteado foi {min(lista)}')
