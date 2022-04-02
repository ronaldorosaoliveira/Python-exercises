# Refaça o Desafio 009 mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for

n = int(input('Digite um número e veja sua Tabuada: '))
for c in range(1,11):
    print(f'{n} x {c} = {n * c}')