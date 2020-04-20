def metade(num=0):
    metade = num / 2
    return metade


def dobro(num=0):
    dobro = num * 2
    return dobro


def aumentar(num=0, porcento=0):
    aumentar = ((porcento / 100) * num) + num
    return aumentar


def diminuir(num=0, porcento=0):
    diminuir = num - ((porcento / 100) * num)
    return diminuir


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
