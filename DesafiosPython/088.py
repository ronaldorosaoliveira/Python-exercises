# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
print('-=' * 30)
print('                    JOGO DA MEGA SENA')
print('-=' * 30)
print()
lista = []
jogos = []
quantidade = int(input('Quantos jogos você quer sortear? '))
print()
totaljogos = 1
while totaljogos <= quantidade:
    contador = 0
    while True:
        num = randint(0,60)
        if num not in lista:
            lista.append(num)
            contador += 1
        if contador == 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    totaljogos += 1
print('-=' * 4, f'Sorteando {quantidade} jogo(s)', '-=' * 4)
print()
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print()
print('-='*5, '< BOA SORTE >', '-='*5)