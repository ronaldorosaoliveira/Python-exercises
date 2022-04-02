# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
# A média de idade do grupo
# Qual o nome do homem mais velho
# Quantas mulheres tem menos de 20 anos
soma = 0
media = 0
maioridadehomem = 0
nomevelho = ''
totalmulher20 = 0
for c in range(1,5):
    print(f'----- {c}ª Pessoa -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('M/F: ')).strip()
    soma += idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totalmulher20 += 1
media = soma / 4
print(f'A média de idade desse grupo é : \033[34m{media}\033[m')
print(f'O homem mais velho tem \033[34m{maioridadehomem}\033[m anos e se chama \033[34m{nomevelho}\033[m')
print(f'Neste grupo existem \033[34m{totalmulher20}\033[m mulheres com menos de 20 anos')
