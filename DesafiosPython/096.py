# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(a,b):
    print(f'A área de um terreno de {a} metros x {b} metros é igual a {a*b} m²')


print('-=' *15)
print('     Controle de Terrenos')
print('-=' *15)
a = float(input('Largura (m): '))
b = float(input('Comprimento (m): '))
area(a,b)