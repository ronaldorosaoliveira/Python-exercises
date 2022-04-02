# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120
from math import factorial
n = int(input('Digite um número e descubra seu Fatorial: '))
f = factorial(n)
print(f'O Fatorial de {n} é {f} !')