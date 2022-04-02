# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('='*50)
print('Caixa Eletrônico 24 Horas'.center(50))
print('='*50)
print('\nCédulas Disponíveis: R$ 50,00 R$ 20,00 R$ 10,00 e R$ 1,00')
valor = int(input('\nQual o valor que será sacado ? '))
total = valor
cedulas = 50
totalcedulas = 0
while True:
    if total >= cedulas:
        total -= cedulas
        totalcedulas += 1
    else:
        if totalcedulas > 0:
            print(f'\nTotal de {totalcedulas} cédulas de R$ {cedulas:.2f}')
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 1
        totalcedulas = 0
        if total == 0:
            break
print('\nObrigado e Volte Sempre !')