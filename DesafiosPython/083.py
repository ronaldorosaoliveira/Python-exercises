# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

frase = str(input('Digite uma expressão matemática: '))
lista = []
for p in frase:
    if p == '(':
        lista.append('(')
    elif p == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão está válida')
else:
    print('Sua expressão é inválida')
