# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

m = float(input('Digite um valor em metro: '))
dm = m * 10
cm = m * 100
mm = m * 1000
dam = m / 10
hm =  m / 100
km = m / 1000
print(f'{m} metro(s) equivalem a {dm} decímetos, {cm} centímetros e {mm} milímetros.')
print(f'{m} metro(s) equivalem a {dam} decâmetros, {hm} hectômetros e {km} quilômetros.')
