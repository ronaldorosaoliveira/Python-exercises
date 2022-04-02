# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    continua = str(input('Quer continuar ? [S/N]: ')).lower()
    if continua in 'n':
        break
print(f'\nVocê digitou {len(lista)} número(s)')
lista.sort(reverse=True)
print(f'\nOs valores digitados em ordem decrescente foram {lista}')
if 5 in lista:
    print('\nO número 5 está incluso na lista !')
else:
    print('\nO número 5 NÃO está incluso na lista !')
