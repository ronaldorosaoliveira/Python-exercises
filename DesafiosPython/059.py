#Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
from time import sleep
primeiro = int(input(f'Digite o 1º valor: '))
segundo = int(input(f'Digite o 2º valor: '))
opcao = 0
while opcao != 5:
    print('[1] Soma\n[2] Multiplicação\n[3] Qual é maior\n[4] Novos números\n[5] Sair')
    opcao = int(input('Digite a opção desejada: '))
    if opcao == 1:
        soma = primeiro + segundo
        print(f'A soma entre {primeiro} e {segundo} é igual a {soma}')
    elif opcao == 2:
        multiplicacao = primeiro * segundo
        print(f'A multiplicação entre {primeiro} e {segundo} é igual a {multiplicacao}')
    elif opcao == 3:
        if primeiro > segundo:
            print(f'O número {primeiro} é maior do que o número {segundo} !')
        elif segundo > primeiro:
            print(f'O número {segundo} é maior do que o número {primeiro} !')
        else:
            print('Os números são iguais !')
    elif opcao == 4:
        print('Digite novos números:')
        primeiro = int(input(f'Digite o 1º valor: '))
        segundo = int(input(f'Digite o 2º valor: '))
    elif opcao == 5:
        print('Finalizando... !')
        sleep(2)
    else:
        print('Opção inválida. Digite novamente.')
    print('=-' * 10)
print('Fim do Programa. Volte Sempre !')