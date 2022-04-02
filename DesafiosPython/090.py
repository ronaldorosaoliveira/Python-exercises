# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

tudo = {}
tudo['nome'] = str(input('Nome: '))
tudo['media'] = float(input(f'Média de {tudo["nome"]}: '))
if tudo['media'] >= 6:
    tudo['situação'] = 'Aprovado'
elif 4 <= tudo['media'] < 6:
    tudo['situação'] = 'Recuperação'
else:
    tudo['situação'] = 'Reprovado'
print('-='*30)
print()
for k, v in tudo.items():
    print(f'{k} é igual a {v}')



