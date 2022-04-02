#Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o

soma = 0
contador = 0
for c in range(1,7):
    n = int(input(f'Digite o {c}º número: '))
    if n % 2 == 0:
        soma += n
        contador += 1
print(f'\nVocê informou {contador} números PARES e a soma entre eles é igual a {soma}')
