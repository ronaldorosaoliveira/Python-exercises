# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários > 1250, calcule um aumento de 10%. Para <=, o aumento é 15%

salario = int(input(f'Digite o seu salário: R$ '))
if salario <= 1250:
    print(f'O seu salário teve um aumento de 15% e agora voce passará a receber R$ {(salario * 0.15) + salario:.2f}')
else:
    print(f'O seu salário teve um aumento de 10% e agora voce passará a receber R$ {(salario * 0.10) + salario:.2f}')
