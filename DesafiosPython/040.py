# Crie um programa que leia 2 notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5: Reprovado
# Média entre 5 e 6.9: Recuperação
# Média maior ou igual a 7: Aprovado

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2

if (nota1 + nota2) / 2 >= 7:
    print(f'Sua média foi {media:.2f}. Parabéns, você foi Aprovado !')
elif (nota1 + nota2) / 2 < 5:
    print(f'Sua média foi {media:.2f}. Infelizmente você foi Reprovado. Estude mais !')
else:
    print(f'Sua média foi {media:.2f}. Você está de Recuperação. Estude para a prova !')
