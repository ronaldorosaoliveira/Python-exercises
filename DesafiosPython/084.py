# Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

lista = []
principal = []
maior = menor = 0
while True:
    lista.append(str(input('Nome: ')))
    lista.append(float(input('Peso(Kg): ')))
    if len(principal) == 0:
        maior = menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista[1]
    principal.append(lista[:])
    lista.clear()
    continua = str(input('Quer continuar ? [S/N]: ')).lower()
    if continua in 'n':
        break
print(f'Foram cadatradas {len(principal)} pessoa(s)')
print(f'O maior peso foi de {maior} Kg. Peso de ', end='')
for p in principal:
    if p[1] == maior:
        print(f'{[p[0]]}', end='')
print(f'\nO menor peso foi de {menor} Kg. Peso de ', end='')
for p in principal:
    if p[1] == menor:
        print(f'{[p[0]]}', end='')