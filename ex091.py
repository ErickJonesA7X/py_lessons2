from random import randint
from operator import itemgetter
from time import sleep

valores = {}
cont = 0

valores['jogador1'] = randint(1, 6)
valores['jogador2'] = randint(1, 6)
valores['jogador3'] = randint(1, 6)
valores['jogador4'] = randint(1, 6)

print('Valores Sorteados:')
for k, v in valores.items():
    print(f'O {k} tirou {v}')
    sleep(1)
print('='*70)
print('== Ranking dos Jogadores ==')
for k, v in sorted(valores.items(), key = itemgetter(1), reverse = True):
    cont += 1
    print(f'{cont}° lugar: {k} com {v}.')
    sleep(1)
#print(sorted(valores.items(), key = itemgetter(1), reverse = True))