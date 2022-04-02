# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triãngulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot
n = int(input('Digite o cateto oposto do Triângulo: '))
m = int(input('Digite o cateto adjacente do Triângulo: '))
print(f'A Hipotenusa desse triângulo é igual a {hypot(n,m)}')
