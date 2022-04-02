# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
# Exemplo:
# Digite um número: 1234
# Unidade: 4
# Dezena: 3
# Centena: 2
# Milhar: 1

n = int(input('Digite um número entre 0 e 9999: '))
unidade = n // 1 % 10 # divide o número por 1 e mostra o resto da divisão inteira por 10
dezena = n // 10 % 10 # divide o número por 10 e mostra o resto da divisão inteira por 10
centena = n // 100 % 10 # divide o número por 100 e mostra o resto da divisão inteira por 10
milhar = n // 1000 % 10 # divide o número por 1000 e mostra o resto da divisão inteira por 10
print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')