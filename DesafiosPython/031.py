# Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens até 200 km e R$ 0,45 para viagens mais longas

n1 = int(input('Qual a distância da sua viagem: '))
if n1 <= 200:
    print(f'O valor da sua viagem é de R$ {n1 * 0.5:.2f} reais')
else:
    print(f'O valor da sua viagem é de R$ {n1 * 0.45:.2f} reais')
