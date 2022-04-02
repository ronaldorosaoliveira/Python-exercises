# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
print('='*50)
print('Jogo do PAR ou ÍMPAR'.center(50))
print('='*50)
v = 0
from random import randint
while True:
    jogador = int(input('Digite um número: '))
    pc = randint(0 , 10)
    total = jogador + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar ? ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {pc}. Total de {total}', end='')
    print(f' ... e {total} é PAR' if total % 2 == 0 else f' ... e {total} é ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU !!!')
            v += 1
        else:
            print('Você PERDEU !!! ')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU !!!')
            v += 1
        else:
            print('Você PERDEU !!!')
            break
    print('Vamos jogar novamente ...')
print(f'GAME OVER. Você venceu {v} vezes.')
