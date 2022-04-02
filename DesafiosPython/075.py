# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

n = int(input('Digite o 1º valor: ')), int(input('Digite o 2º valor: ')), int(input('Digite o 3º valor: ')), int(input('Digite o 4º valor: '))
print(f'\nVocê digitou os seguintes valores: {n}')
if 9 in n:
    print(f'\nO número 9 apareceu {n.count(9)} vez(es)')
else:
    print('\nO número 9 não foi digitado')
if 3 in n:
    print(f'\nO número 3 apareceu pela primeira vez na {n.index(3)+1}ª posição')
else:
    print('\nO número 3 não foi digitado')

print('\nOs números pares nessa lista são:', end=' ')
for c in n:
    if c % 2 == 0:
        print(f'{c}', end=' ')
if c % 2 != 0:
    print('Não existem números pares nesa lista', end=' ')