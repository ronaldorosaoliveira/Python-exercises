# Refaça a tabuada feita anteriormente, só que agora ela só vai funcionar se for digitado um número, caso contrário, ela
# mostrará a seguinte mensagem: "Erro! Digite um númeto inteiro!"

def título(msg):
    tam = len(msg) + 4
    print('=' * tam)
    print(f'  {msg}')
    print('=' * tam)


def tabuada(msg):
    print('='*50)
    while True:
        try:
            n = int(input(msg))
        except:
            print('\033[1;31mErro. Digite um número inteiro !\033[m')
        else:
            break
    print('='*50)
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
    print('='*50)


def continua(msg):
    while True:
        continua = str(input(msg))
        if continua in 'Nn':
            print('='*50)
            print('Programa Tabuada Finalizado !')
            print('=' * 50)
            break
        elif continua in 'sS':
            tabuada('Digite um número e descubra sua Tabuada: ')
        else:
            print('\033[1;31mErro! Digite [S] ou [N]\033[m')


título('PROGRAMA TABUADA')
tabuada('Digite um número e descubra sua Tabuada: ')
continua('Quer continuar [S/N] ? ')
