# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra 'SANTO".
cidade = str(input('Digite o nome de uma cidade: ')).strip()
min = cidade.lower()
print('santo' in min)
