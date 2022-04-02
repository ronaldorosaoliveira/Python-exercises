# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos
# ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado

vcasa = float(input('Digite o valor da casa: R$ '))
salario = float(input('Digite seu salário: R$ '))
ano = int(input('Digite em quantos anos você quer pagar a casa: '))
meses = ano*12

print(f'\nO valor da prestação mensal em {meses} meses será de: R$ {vcasa/meses:.2f}')

if vcasa/meses > salario*0.3:
    print('Infelizmente nós não podemos fazer esse empréstimo pra você !')
else:
    print('Parabéns, você foi está dentro de nossas condições e terá o empréstimo conosco !!!')

