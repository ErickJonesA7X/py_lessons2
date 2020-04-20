def metade(num=0, formato=False):
    metade = num / 2
    return metade if formato is False else moeda(metade)


def dobro(num=0, formato=False):
    dobro = num * 2
    return dobro if formato is False else moeda(dobro)


def aumentar(num=0, porcento=0, formato=False):
    aumentar = ((porcento / 100) * num) + num
    return aumentar if formato is False else moeda(aumentar)


def diminuir(num=0, porcento=0, formato=False):
    diminuir = num - ((porcento / 100) * num)
    return diminuir if formato is False else moeda(diminuir)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
