# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
contador = 0
soma = 0
n = 0
n = int(input('Digite um número (999 para Parar): '))
while n != 999:
    contador += 1
    soma += n
    n = int(input('Digite um número (999 para Parar): '))
print(f'Você digitou {contador} números e a soma deles é igual a {soma}')