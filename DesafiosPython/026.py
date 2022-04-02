# Faça um programa que leia a frase pelo teclado e mostre:
# Quantas vezes a parece a letra 'A'
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez

frase = str(input('Digite uma frase: ')).strip()
frase2 = frase.lower()
print(f'A letra a aparece {frase2.count("a")} vezes na frase')
print(f'A letra a aparece pela primeira vez na posição {frase2.find("a")+1 - frase2.count(" ")}')
print(f'A letra a aparece pela última vez na posição {frase2.rfind("a")+1 - frase2.count(" ")}')
