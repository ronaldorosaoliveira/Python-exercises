# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

n = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a Razão da PA: '))
termo = n
contador = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while contador <= total:
        print(f'{termo}' , end=' ➝ ')
        contador += 1
        termo += razao
    print('Pausa ...')
    mais = int(input('Mais quantos termos você quer mostrar? '))
print('Fim')
print(f'progressão finalizada com {total} termos mostrados!')
