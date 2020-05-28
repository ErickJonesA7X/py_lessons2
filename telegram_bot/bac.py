class Cliente:

    def __init__(self, nome):
        self.nome = nome



class Pessoa:

    def __init__(self, nome):
        self.nome = nome


p1 = Pessoa('Érick')

c1 = Cliente('Tarcisio')


def abc(argumento):
    print(argumento.nome)


abc(c1)
abc(p1)