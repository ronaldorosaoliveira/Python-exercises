# Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possíveis sobre ele

palavra = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(palavra))
print('Só tem espaços? ', palavra.isspace())
print('É um número? ', palavra.isnumeric())
print('É alfabético? ', palavra.isalpha())
print('É alfanumérico? ', palavra.isalnum())
print('Está em maiúsculas?', palavra.isupper())
print('Está em minúsculas?', palavra.islower())
print('Está capitalizada?', palavra.istitle())