# Desenvola um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triângulo

r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
if r1+r2 > r3 and r2+r3 > r1 and r1+r3 > r2:
    print('Esses três segmentos formam um triângulo !!!')
else:
    print('Esses três segmentos NÃO formam um triângulo !!!')