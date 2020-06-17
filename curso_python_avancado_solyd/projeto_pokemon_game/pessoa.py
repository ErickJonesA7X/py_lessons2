import random
from pokemon import *

NOMES = [
        'João', 'Isabela', 'Lorena', 'Francisco', 'Ricardo', 'Diego',
        'Patricia', 'Marcelo', 'Gustavo', 'Gerônimo', 'Gary'
    ]

POKEMONS = [
    PokemonFogo('Charmander'),
    PokemonFogo('Flarion'),
    PokemonFogo('Charmilion'),
    PokemonEletrico('Pikachu'),
    PokemonEletrico('Raychu'),
    PokemonAgua('Squirtle'),
    PokemonAgua('Magicarp'),
]


class Pessoa:


    def __init__(self, nome=None, pokemons=[]):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.pokemons = pokemons

    def __str__(self):
        return self.nome


    def mostrar_pokemons(self):
        if self.pokemons:
            print(f'Pokémons de {self}')
            for pokemon in self.pokemons:
                print(pokemon)
        else:
            print(f'{self} não tem nenhum pokémon!')

class Player(Pessoa):
    tipo = 'player'

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print(f'{self} capturou {pokemon}')


class Inimigo(Pessoa):
    tipo = 'inimigo'

    def __init__(self, nome=None, pokemons=[]):
        if not pokemons:
            for i in range(random.randint(1, 6)):
                pokemons.append(random.choice(POKEMONS))


        super().__init__(nome=nome, pokemons=pokemons)


meu_inimigo = Inimigo()
print(meu_inimigo)
meu_inimigo.mostrar_pokemons()