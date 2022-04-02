# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.corinthians.com.br/')
except urllib.error.URLError:
    print('\nO site não está acessível no momento !')
else:
    print('\nO site encontra-se acessível !')
