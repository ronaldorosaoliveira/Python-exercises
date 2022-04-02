# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

print('='*50)
print('CADASTRO DE UMA PESSOA'.center(50))
print('='*50)
total18 = 0
homem = 0
mulher = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    if idade >= 18:
        total18 += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar ? [S/N]: ')).upper().strip()[0]
    if resposta == 'N':
        break
print(f'Total de Pessoas com mais de 18 anos: {total18}\nAo todo temos {homem} homens cadastrados.\nE temos {mulher} mulher(es) com menos de 20 anos')


