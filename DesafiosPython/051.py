# Desenvolva um programa que leia o primeiro termo e uma razão de uma PA. No final, mostre os 10 primeiros termos dessa progresão.

n = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a Razão da PA: '))
decimo = n + (10 - 1) * razao
for c in range(n, decimo + razao , razao):
    print(f'{c}' , end=' ➝ ')
print('Acabou !')