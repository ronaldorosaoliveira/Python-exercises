# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
from time import sleep
ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1 , nota2], media])
    resposta = str(input('Quer coninuar ? [S/N]')).lower()
    if resposta in 'n':
        break
print('-='*30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-='*30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-='* 35)
    alunos = int(input('Mostrar notas de qual aluno? [999 para finalizar]: '))
    if alunos == 999:
        print('Finalizando ...')
        sleep(2)
        break
    if alunos <= len(ficha) - 1:
        print(f'Notas de {ficha[alunos][0]} são {ficha[alunos][1]}')
print('<<< VOLTE SEMPRE >>>')