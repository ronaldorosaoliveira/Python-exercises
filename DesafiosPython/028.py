# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo PC.
# O prorama deverá escrever na tela se o usuário venceu ou perdeu
from random import randint
from time import sleep # tempo de espera para aparecer a próxima linha
print('JOGO DA ADIVINHAÇÃO')
pc = randint(0, 5)
n1 = int(input('Vou pensar em um número de 0 a 5. Tente adivinhar: '))
print('PROCESSANDO ...')
sleep(3)
print(f'O número escolhido pelo Computador foi : {pc}')
if n1 == pc:
    print('Parabéns, você leu a mente do Computador !!!')
else:
    print('O computador venceu desta vez')
