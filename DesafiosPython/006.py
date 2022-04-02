# Crie um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada

n1 = int(input('Digite um número: '))
n2 = n1 * 2
n3 = n1 * 3
n4 = n1 ** (1/2)
print(f' O dobro de {n1} é {n2}, o triplo de {n1} é {n3} e a raiz quadrada de {n1} é {n4:.3f}')

# (:.3f) significa quantas casas após a virgula queremos deixar -> ' 1,333 '
# print (:20) significa que o caracter ficará com 20 espaços -> 'Ana                 '
# print (:^20) significa que o caracter ficará com 20 espaços centralizado -> '        Ana         '
# print (:>20) significa que o caracter ficará com 20 espaços alinhado á direita -> '                 Ana'
# print (:<20) significa que o caracter ficará com 20 espaços alinhado á esquerda -> 'Ana                 '
# print (:=^20) significa que o caracter ficará com 20 espaços centralizado com = -> '===========Ana=========='

