import curso_python_avancado_solyd
from curso_python_avancado_solyd.projeto_pokemon_game.pokemon import *
from curso_python_avancado_solyd.projeto_pokemon_game.pessoa import *


def escolher_pokemon_inicial(player):
    print(f'Olá {player}, vocÊ poderá escolher agora o Pokémon que irá lhe acompanhar nessa jornada!')

    pikachu = PokemonEletrico('Pikachu', level=1)
    charmander = PokemonFogo('Charmander', level=1)
    squirtle = PokemonAgua('Squirtle', level=1)

    print('Você possui 3 escolhas: ')
    print('1 - Pikachu')
    print('2 - Charmander')
    print('3 - Squirtle')

    while True:
        escolha = int(input('Escolha o seu Pokémon: '))

        if escolha == 1:
            player.capturar(pikachu)
            break
        elif escolha == 2:
            player.capturar(charmander)
            break
        elif escolha == 3:
            player.capturar(squirtle)
            break
        else:
            print('Escolha inválida! Por favor digite uma nova opção.')


player = Player('Guilherme')
player.capturar(PokemonFogo('Charmander', level=1))

inimigo1 = Inimigo(nome='Gary', pokemons=[PokemonAgua('Squirtle', level=1)])

player.batalhar(inimigo1)