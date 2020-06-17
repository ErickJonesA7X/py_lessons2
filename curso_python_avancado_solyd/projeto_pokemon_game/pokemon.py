import random


class Pokemon:    #Classe abstrata  (O Pai)
    def __init__(self, especie, level=random.randint(1, 100), nome=None):
        self.especie = especie
        self.level = level

        if nome:
            self.nome = nome
        else:
            self.nome = especie
            

    def __str__(self):
        return f'{self.nome}({self.level})'


    def atacar(self, pokemon):
        print(f'{self} atacou {pokemon}')


class PokemonEletrico(Pokemon):
    tipo = 'elétrico'


    def atacar(self, pokemon):
        print(f'{self}lançou um raio do trovão em {pokemon}')


    def dar_choque(self):
        print('Deu choque!')


class PokemonFogo(Pokemon):
    tipo = 'fogo'

    def atacar(self, pokemon):
        print(f'{self}lançou uma bola de fogo na cabeça do {pokemon}')


class PokemonAgua(Pokemon):
    tipo = 'água'

    def atacar(self, pokemon):
        print(f'{self} lançou um jato de água em {pokemon}')




