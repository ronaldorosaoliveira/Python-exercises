# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
# Ex:
# escreva(‘Olá, Mundo!’)
# Saída:
# ~~~~~~~~~
# Olá, Mundo!
# ~~~~~~~~~


#def escreva(texto):
#    print('='* len(texto))
#    print(texto)
#    print('='* len(texto))

def escreva(texto):
    tam = len(texto) + 4
    print('=' * tam)
    print(f'  {texto}')
    print('=' * tam)


escreva('Ronaldo Rosa de Oliveira')
escreva('Camila Shimada Pandolpho')
escreva('Olá Mundo !')
escreva('Oi')
