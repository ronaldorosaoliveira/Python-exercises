# Escreva um programa que leia a velocidade de um carro. Se ele passar de 80 km/h, mostre uma mensagem que ele foi multado.
# A multa vai custar R$ 7,00 por cada km acima do limite

km = int(input('Você está dirigindo em uma rodovia. Qual a sua velocidade ? '))
multa = (km - 80) * 7
if km > 80:
    print(f'Você levou uma multa e vai pagar o valor de R$ {multa} reais !')
else:
    print('Dirija com segurança !')