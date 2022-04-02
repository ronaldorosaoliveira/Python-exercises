# Desenvolva um lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida

altura = float(input('Digite a sua altura em cm: '))
peso = float(input('Digite seu peso em kg: '))
imc = (peso) / ((altura/100)** 2)
if imc < 18.5:
    print(f'Seu IMC é igual a {imc:.2f}. Você está abaixo do peso ideal')
elif imc >= 18.5 and imc <= 25:
    print(f'Seu IMC é igual a {imc:.2f}. Você está no Peso Ideal !')
elif imc > 25 and imc <= 30:
    print(f'Seu IMC é igual a {imc:.2f}. Você está no Acima do peso !')
elif imc > 30 and imc <= 40:
    print(f'Seu IMC é igual a {imc:.2f}. Você está Obeso !')
else:
    print(f'Seu IMC é igual a {imc:.2f}. Você está no com Obesidade Mórbida !')