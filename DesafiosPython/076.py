# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

lista = ('Lápis', 1,
         'Borracha', 1,
         'Caneta', 2,
         'Apontador', 1.50,
         'Caderno', 10.00,
         'Lapiseira', 5.00)
print('=' *48)
print(f'{"Listagem de Preços":^40}')
print('='*48)
for posicao in range(0, len(lista)):
    if posicao % 2 == 0:
        print(f'{lista[posicao]:.<40}', end='')
    else:
        print(f'R$ {lista[posicao]:>5.2f}')
print('=' * 48)