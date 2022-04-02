# Crie um programa que faça o computador jogar jokenpô com você !
from random import randint
print('{:=^50}'.format(' Jogo do Pedra, Papel ou Tesoura '))
print('Suas opções:\n [1] Pedra \n [2] Papel\n [3] Tesoura')
n = int(input('Digite a opção desejada: '))
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0,2)
if n == 1 and pc == 0:
    print(f'Você escolheu Pedra e o computador escolheu {itens[pc]}. Deu EMPATE !')
elif n == 1 and pc == 1:
    print(f'Você escolheu Pedra e o computador escolheu {itens[pc]}. O Computador VENCEU !')
elif n == 1 and pc == 2:
    print(f'Você escolheu Pedra e o computador escolheu {itens[pc]}. Você VENCEU !')

elif n == 2 and pc == 0:
    print(f'Você escolheu Papel e o computador escolheu {itens[pc]}. Você VENCEU ! !')
elif n == 2 and pc == 1:
    print(f'Você escolheu Papel e o computador escolheu {itens[pc]}. Deu EMPATE !')
elif n == 2 and pc == 2:
    print(f'Você escolheu Papel e o computador escolheu {itens[pc]}. O Computador VENCEU !')

elif n == 3 and pc == 0:
    print(f'Você escolheu Tesoura e o computador escolheu {itens[pc]}. O Computador VENCEU ! !')
elif n == 3 and pc == 1:
    print(f'Você escolheu Tesoura e o computador escolheu {itens[pc]}. Você VENCEU !')
else:
    print(f'Você escolheu Tesoura e o computador escolheu {itens[pc]}. Deu EMPATE !')