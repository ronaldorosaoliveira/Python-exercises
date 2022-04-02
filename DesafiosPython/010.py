# Crie um programa que leia quanto dinheiro ela tem na carteira e mostre quantos dólares ela pode comprar. Considere US$ 1,00 = R$ 3,27

n1 = float(input('Quantos reais você tem na carteira? R$ '))
n2 = n1 / 3.27
print(f'Com R$ {n1:.2f}, você pode comprar US$ {n2:.2f} !')