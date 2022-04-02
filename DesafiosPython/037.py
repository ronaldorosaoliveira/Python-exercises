# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para não octal
# 3 para hexadecimal

n = int(input('Digite um número inteiro: '))
print('\nEscolha uma das bases para conversão:\n[1] converter para binário\n[2] converter para não octal\n[3] converter para hexadecimal')
n2 = int(input('Sua opção: '))
binario = bin(n)
octal = oct(n)
hexadecimal = hex(n)

if n2 == 1:
    print(f'{n} em binário é: {binario[2:]}')
elif n2 == 2:
    print(f'{n} em não octal é: {octal[2:]}')
elif n2 == 3:
    print(f'{n} em hexadecimal é: {hexadecimal[2:]}')
else:
    print('Digite uma opção válida !')