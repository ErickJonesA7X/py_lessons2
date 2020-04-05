from random import randint
computador = randint(0, 10)
print('-=-'*20)
print('Vou pensar em um número entre 0 e 10. Tente advinhar...')
print('-=-'*20)
acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Em qual número entre 0 e 10 estou pensando agora: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print(f'PARABÉNS!!! Você acertou com {palpites} tentativas.')