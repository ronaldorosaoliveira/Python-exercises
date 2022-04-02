# Escreva um programa que leia 2 nºs inteiros e compare-os, mostrando na tela uma mensagem:
# O 1º valor é maior
# O 2º valor é maior
# Não existe valor maior, os dois são iguais

n = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n > n2:
    print(f'{n} é maior do que {n2}')
elif n2 > n:
    print(f'{n2} é maior que {n}')
else:
    print('Não existe valor maior, os dois são iguais !')