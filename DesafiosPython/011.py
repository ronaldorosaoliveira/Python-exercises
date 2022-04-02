# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade
# de tinta necesária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²

n1 = float(input('Digite a Altura da sua parede em metro(s): '))
n2 = float(input('Digite a largura da sua parede em metro(s): '))
n3 = n1 * n2
n4 = n3 / 2
print(f'A área total da sua parede é de {n3} metro(s) quadrados e serão necessários {n4} litro(s) de tinta para pintá-la')