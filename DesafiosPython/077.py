# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

lista = ('Abacate', 'Maça', 'Banana', 'Goiaba', 'Limao', 'Amora', 'Abacaxi', 'Mexerica', 'Laranja')

for p in lista:
    print(f'\nNa palavra {p.upper()} temos as segintes vogais: ', end='')
    for letra in p:
        if letra.lower() in  'aeiou':
            print(letra.lower(), end=' ')