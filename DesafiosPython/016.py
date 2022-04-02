# Crie um programa que leia um nº real qualquer pelo teclado e mostre na tela a sua porção inteira

from math import trunc
n = float(input('Digite um número: '))
print(f'O número {n} tem a parte inteira {trunc(n)}')


