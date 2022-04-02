# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

n = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a Razão da PA: '))
termo = n
contador = 1
while contador < 11:
    print(f'{termo}' , end=' ➝ ')
    contador += 1
    termo += razao
print('Acabou !')