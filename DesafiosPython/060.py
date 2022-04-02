# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

n = int(input('Digite um número e descubra seu Fatorial: '))
fatorial = 1
c = 2
while c <= n:
    fatorial = fatorial * c
    c += 1
print(f'O valor de {n}! é igual a {fatorial}')