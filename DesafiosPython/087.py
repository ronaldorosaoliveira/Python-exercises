# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [ [0, 0, 0],
           [0, 0, 0],
           [0, 0, 0] ]
somapar = maiorlinha = somacoluna = 0
print('Digite um valor para a posição [L, C]')
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para a posição [{linha+1}, {coluna+1}]: '))
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            somapar += matriz[linha][coluna]
    print()
print()
print(f'A soma dos valores PARES digitados é igual a: {somapar}')
for linha in range(0,3):
    somacoluna += matriz[linha][2]
print(f'A soma dos valores da coluna 3 é igual a: {somacoluna}')
for coluna in range(0,3):
    if coluna == 0:
        maiorlinha = matriz[1][coluna]
    elif matriz[1][coluna] > maiorlinha:
        maiorlinha = matriz[1][coluna]
print(f'O maior valor da segunda linha é igual a: {maiorlinha}')