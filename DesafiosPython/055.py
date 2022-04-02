# Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lido.
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'Digite o peso da {c}ª pessoa (em Kg): '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O MAIOR peso lido foi {maior} Kg')
print(f'O MENOR peso lido foi {menor} Kg')
