from random import randint
computador = randint(0, 5)
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-'*20)
jogador = int(input('Em qual número entre 0 e 5 estou pensando agora: '))

if jogador == computador:
    print('PARABÉNS!!!  Você conseguiu me vencer!!!')
else:
    print(f'GANHEI!!!  Eu pensei no número {computador} e não no {jogador}')
