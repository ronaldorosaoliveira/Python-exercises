# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []
while True:
    n = (int(input('Digite um número: ')))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso !')
    else:
        print('Valor já inserido. Não vou adicionar !')
    continua = (str(input('Quer continuar? [S/N]: '))).lower()
    if continua in 'n':
        break
lista.sort()
print(f'Você digitou os valores {lista}')

