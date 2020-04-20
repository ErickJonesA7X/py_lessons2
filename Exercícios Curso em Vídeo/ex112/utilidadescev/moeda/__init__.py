def metade(num=0, formato=False):
    metade = num / 2
    return metade if formato is False else moeda(metade)


def dobro(num=0, formato=False):
    dobro = num * 2
    return dobro if formato is False else moeda(dobro)


def aumentar(num=0, porc1=0, formato=False):
    aumentar = ((porc1 / 100) * num) + num
    return aumentar if formato is False else moeda(aumentar)


def diminuir(num=0, porcento=0, formato=False):
    diminuir = num - ((porcento / 100) * num)
    return diminuir if formato is False else moeda(diminuir)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(num=0, porc1=0, porc2=0):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(num)}')
    print(f'Dobro do preço: \t{dobro(num, True)}')
    print(f'Metade do preço: \t{metade(num, True)}')
    print(f'{porc1}% de aumento: \t{aumentar(num, porc1, True)}')
    print(f'{porc2}% de redução: \t{diminuir(num, porc2, True)}')
    print('-' * 30)
