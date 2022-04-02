# Crie um programa que leio o nome completo de uma pessoa e mostre:
# - o nome com todas as letras MAIÚSCULAS
# - o nome com todas as letras minúsculas
# - Quantas letras tem ao tod o, sem considerar os espaços
# - Quantas letras o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando dados ...')
print(f'Seu nome em MAIÚSCULAS é: {nome.upper()}')
print(f'Seu nome em MAIÚSCULAS é: {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras.')
print(f'Seu primeiro nome tem {nome.find(" ")} letras.')