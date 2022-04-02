def aumentar(preço=0, taxa=0, formato=False):
    res = preço + (preço * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(preço = 0, taxa = 0, formato=False):
    res = preço - (preço * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(preço = 0, formato=False):
    res = preço * 2
    return res if not formato else moeda(res)


def metade(preço = 0, formato=False):
    res = preço / 2
    return res if formato is False else moeda(res)


def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda} {preço:.2f}'.replace('.', ',')

def resumo(preço=0, taxaaumento=10, taxaredução=10):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço Analisado: {moeda(preço)}'.center(30))
    print('-'*30)
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'{taxaaumento}% de aumento: \t{aumentar(preço, 10, True)}')
    print(f'{taxaredução}% de redução: \t{diminuir(preço, 10, True)}')
    print('-' * 30)