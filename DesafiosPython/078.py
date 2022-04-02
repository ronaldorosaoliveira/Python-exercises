# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []
maior = menor = 0

for n in range(0,5):
    lista.append(int(input(f'Digite um número para a posição {n}: ')))
    if n == 0:
        maior = menor = lista[n]
    else:
        if lista[n] > maior:
            maior = lista[n]
        if lista[n] < menor:
            menor = lista[n]
print(f'Você digitou os valores {lista}')
print(f'o maior valor digitado foi o valor {maior} nas posições', end=' ')
for i,v in enumerate(lista):
    if v == maior:
        print(f'{i} ...', end=' ')
print(f'\nO menor valor digitado foi o valor {menor} nas posições', end=' ')
for i,v in enumerate(lista):
    if v == menor:
        print(f'{i} ...', end=' ')