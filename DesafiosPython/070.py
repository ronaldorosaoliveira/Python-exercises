#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

print('='*50)
print('LOJAS RONALDINHO'.center(50))
print('='*50)
maisbarato = ' '
contador = 0
menor = 0
maisdemil = 0
total = 0
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço. R$: '))
    total += preço
    contador += 1
    if contador == 1:
        menor = preço
        maisbarato = produto
    else:
        if preço < menor:
            menor = preço
            maisbarato = produto
    if preço > 1000:
        maisdemil += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar ? [S/N]: ')).upper().strip()[0]
    if resposta == 'N':
        break
print(f'O total da compra foi R$ {total:.2f}')
print(f'Você comprou {maisdemil} produto(s) acima de R$ 1000,00')
print(f'O produto mais barato é o(a) {maisbarato} e custa R$ {menor:.2f} ')