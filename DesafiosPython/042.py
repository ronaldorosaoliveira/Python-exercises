# Refaça o desafio 35 dos triângulos acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: Todos os lado iguais
# Isósceles: 2 lados iguais
# Escaleno: Todos os lados diferentes

r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

if r1+r2 > r3 and r2+r3 > r1 and r1+r3 > r2 and r1 == r2 and r1 != r3 and r2 != r3:
    print('Esses três segmentos formam um triângulo Isósceles!!!')
elif r1+r2 > r3 and r2+r3 > r1 and r1+r3 > r2 and r1 == r3 and r1 != r2 and r3 != r2:
    print('Esses três segmentos formam um triângulo Isósceles!!!')
elif r1+r2 > r3 and r2+r3 > r1 and r1+r3 > r2 and r2 == r3 and r1 != r2 and r2 != r3:
    print('Esses três segmentos formam um triângulo Isósceles!!!')

elif r1+r2 > r3 and r2+r3 > r1 and r1+r3 > r2 and r1 == r2 == r3:
    print('\nEsses três segmentos formam um triângulo Equilátero!!!')

elif r1+r2 > r3 and r2+r3 > r1 and r1+r3 > r2 and r1 != r2 != r3 != r1:
    print('Esses três segmentos formam um triângulo Escaleno!!!')

else:
    print('Esses três segmentos NÃO formam um triângulo !!!')
