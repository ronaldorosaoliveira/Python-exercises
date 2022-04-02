# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# À vista: 10% de desconto
# Crédito à vista: 5% de desconto
# 2x no crédito: Preco normal
# 3x ou mais no crédito: 20% de juros
print('{:=^50}'.format(' Lojas Ronaldinho '))
total = float(input('Digite o valor da sua compra: '))
print('Formas de Pagamento:')
print('[1] À vista \n[2] Crédito à vista \n[3] 2x no crédito \n[4] 3x ou mais no crédito')
n = int(input('Selecione a Opção Desejada: '))
avista = total - (total*0.1)
credito1 = total - (total*0.05)
credito3 = total + (total*0.3)
if n == 1:
    print(f'A sua compra no valor de R$ {total:.2f} teve um desconto de 10% e passará a ser R$ {avista:.2f} !')
elif n == 2:
    print(f'A sua compra no valor de R$ {total:.2f} teve um desconto de 5% e passará a ser R$ {credito1:.2f} !')
elif n == 3:
    print(f'A sua compra no valor de R$ {total:.2f} não teve desconto !')
else:
    print(f'A sua compra no valor de R$ {total:.2f} teve juros de 30% e passará a ser {credito3:.2f} !')