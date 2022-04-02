# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um número: ')))
    continua = str(input('Quer continuar ? [S/N]: ')).lower()
    if continua in 'n':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'Você digitou os números: {lista}')
print(f'A lista de PARES é: {pares}')
print(f'A lista de ÍMPARES é: {impares}')