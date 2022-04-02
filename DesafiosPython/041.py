# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: Mirim
# Até 14 anos: Infantil
# Até 19 anos: Júnior
# Até 20 anos: Sênior
# Acima: Master

from datetime import date
n = int(input('Digite o ano do seu nascimento: '))
atual = date.today().year
idade = atual - n
if idade <= 9:
    print(f'Em {atual} você completará {idade} anos. Portanto a sua categoria é Mirim !')
elif idade > 9 and idade <= 14:
    print(f'Em {atual} você completará {idade} anos. Portanto a sua categoria é Infantil !')
elif idade > 14 and idade <= 19:
    print(f'Em {atual} você completará {idade} anos. Portanto a sua categoria é Júnior !')
elif idade > 19 and idade <= 20:
    print(f'Em {atual} você completará {idade} anos. Portanto a sua categoria é Sênior !')
elif idade > 20:
    print(f'Em {atual} você completará {idade} anos. Portanto a sua categoria é Master !')