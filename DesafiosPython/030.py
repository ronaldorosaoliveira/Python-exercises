# Crie um programa que leia um nº inteiro e mostre na tela se ele é par ou ímpar

n = int(input('Digite um número: '))
n2 = n % 2
if n2 == 0:
    print(f'O número {n} é PAR !')
else:
    print(f'O número {n} é ÍMPAR !')