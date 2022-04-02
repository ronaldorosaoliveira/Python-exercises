# Faça um programa que leia um ângulo qualuqer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

from math import sin, cos, tan, radians
n = float(input('Digite um ângulo entre 0º e 360º: '))
seno = sin(radians(n))
cosseno = cos(radians(n))
tangente = tan(radians(n))
print(f'O Seno desse ângulo é igual a {seno:.2f} \nO Cosseno desse ângulo é igual a {cosseno:.2f}  \nA Tangente desse ângulo é igual a {tangente:.2f}')
