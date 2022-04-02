# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

dados = {}
lista = []
soma = media = 0
while True:
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('Por favor, digite apenas M ou F')
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    lista.append(dados.copy())
    while True:
        continua = str(input('Quer continuar ? [S/N]: ')).upper()[0].strip()
        if continua in 'SN':
            break
        print('Por favor, digite apenas S ou N')
    if continua == 'N':
        break
print('-='*30)
print(f'A) Ao todos temos {len(lista)} pessoas cadastradas')
print('-='*30)
media = soma / len(lista)
print(f'B) A média de idade é de {media:.1f} anos')
print('-='*30)
print(f'C) As mulheres cadastradas foram: ', end='')
for p in lista:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end='')
print()
print('-='*30)
print(f'D) Lista das pessoas que estão acima da média: ')
for p in lista:
    if p['idade'] > media:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
print('-='*30)
print('<<<  Encerrado   >>>')
print('-='*30)