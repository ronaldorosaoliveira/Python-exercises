# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
contador = 0
soma = 0
media = 0
maior = 0
menor = 0
confirmacao = 'S'
while confirmacao in 'S':
    n = int(input('Digite um número: '))
    soma += n
    contador += 1
    if contador == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    confirmacao = str(input('Quer continuar ? [S/N]: ')).upper().strip()
    media = soma / contador
print(f'\nVocê digitou {contador} número(s) e a média entre eles foi {media}. O maior valor foi {maior} e o menor valor foi {menor}.')



