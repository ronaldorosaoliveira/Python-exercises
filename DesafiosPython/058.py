# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final
# quantos palpites foram necessários para vencer.

from random import randint
from time import sleep # tempo de espera para aparecer a próxima linha
print('========== JOGO DA ADIVINHAÇÃO v2.0 ==========')
print('Vou pensar em um número de 0 e 10.\nSerá que você consegue adivinhar ?')
pc = randint(0, 10)
contador = 0
acertou = False
while not acertou:
    n1 = int(input('Qual o seu palpite ?: '))
    contador += 1
    if n1 == pc:
        acertou = True
    else:
        if n1 < pc:
            print('PROCESSANDO ...')
            sleep(1)
            print('Mais... tente novamente: ')
        else:
            print('PROCESSANDO ...')
            sleep(1)
            print('Menos... tente novamente')
print('PROCESSANDO ...')
sleep(1)
print(f'Parabéns !!! Você acertou com \033[34m{contador}\033[m tentativas!')