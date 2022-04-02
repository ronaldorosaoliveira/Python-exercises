# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep
def maior(* valores):
    cont = maior = 0
    print('-='* 30)
    print('Analisando os valores informados . . . ')
    for v in valores:
        print(f'{v} ', end=' ')
        sleep(0.4)
        if cont == 0:
            maior = v
        else:
            if v > maior:
                maior = v
        cont += 1
    print(f'Foram informados {cont} valores')
    print(f'O maior valor informado foi {maior}')


maior(9, 5, 4 , 6, 15, 6)
maior(4, 8, 52, 4, 5)
maior(8, 20, 3, 4)
maior(4,3)
maior(1)
maior()