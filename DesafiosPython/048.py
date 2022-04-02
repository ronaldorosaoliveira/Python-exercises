# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 e que se encontram no intervalo de 1 até 500

soma = 0
contador = 0
for c in range(1,501, 2):
    if c % 3 == 0:
        contador += + 1 # contador = contador + 1
        soma  += + c # soma = soma + c
print(f'\nA soma de todos os {contador} valores solicitados é igual a {soma}')