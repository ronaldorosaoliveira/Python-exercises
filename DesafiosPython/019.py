# Um professor quer sortear um dos seus 4 alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random
n1 = str(input(' Nome do primeiro aluno: '))
n2 = str(input(' Nome do segundo aluno: '))
n3 = str(input(' Nome do terceiro aluno: '))
n4 = str(input(' Nome do quarto aluno: '))
lista = [n1,n2,n3,n4]
print(f'O escolhido a apagar a lousa foi ... : {random.choice(lista)}')