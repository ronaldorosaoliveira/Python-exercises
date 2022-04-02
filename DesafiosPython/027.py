# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
# Exemplo: Ana Maria de Souza
# Primeiro: Ana
# Último: Souza

nome = str(input('Digite seu nome completo: ')).strip()
nome2 = nome.split()
print(f'Seu primeiro nome é: {nome2[0]}')
print(f'Seu último nome é: {nome2[len(nome2) - 1]}') # len(nome2) vai mostrar quantas posições tem nome2 e escrito dessa maneira, ele vai mostrar o nome2 menos -1 posição, que no caso é a última.

