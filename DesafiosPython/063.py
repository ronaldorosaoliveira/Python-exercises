# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
# Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8

n = int(input('Digite quantos termos da sequencia de Fibonacci você quer mostrar: '))
n1 = 0
n2 = 1
print(f'{n1} -> {n2}', end=' ')
contador = 3
while contador <= n:
    n3 = n1 + n2
    print(f'-> {n3}', end=' ' )
    n1 = n2
    n2 = n3
    contador += 1
print('-> Fim')