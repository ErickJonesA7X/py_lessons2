import random


class Pokemon:    #Classe abstrata  (O Pai)
    def __init__(self, especie, level=None, nome=None):
        self.especie = especie

        if level:
            self.level = level
        else:
            self.level = random.randint(1, 100)

        if nome:
            self.nome = nome
        else:
            self.nome = especie

        self.ataque = self.level * 5
        self.vida = self.level * 10

    def __str__(self):
        return f'{self.nome}({self.level})'


    def atacar(self, pokemon):
        pokemon.vida -= self.ataque
        print(f'{pokemon_inimigo} perdeu {self.ataque} pontos de vida.')


class PokemonEletrico(Pokemon):
    tipo = 'elétrico'


    def atacar(self, pokemon):
        print(f'{self}lançou um raio do trovão em {pokemon}')
        super().atacar(pokemon)

    def dar_choque(self):
        print('Deu choque!')


class PokemonFogo(Pokemon):
    tipo = 'fogo'

    def atacar(self, pokemon):
        print(f'{self}lançou uma bola de fogo na cabeça do {pokemon}')
        super().atacar(pokemon)

class PokemonAgua(Pokemon):
    tipo = 'água'

    def atacar(self, pokemon):
        print(f'{self} lançou um jato de água em {pokemon}')
        super().atacar(pokemon)


