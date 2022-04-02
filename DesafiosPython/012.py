# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

n1 = float(input('Digite o valor do produto desejado em R$: '))
n2 = n1 - n1 * 0.05
print(f'O preço deste produto com desconto de 5% é R$ {n2}')