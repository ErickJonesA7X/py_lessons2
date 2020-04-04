from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('\033[7;34;m-=-\033[m'*11)
print("{:^45}".format ("\033[1;33;44mVAMOS JOGAR JOKÉNPO!!!\033[m"))
print('\033[1;33;m-=-\033[m'*11)

print("""Escolha uma Opção:
[ 0 ] PEDRA (JO)
[ 1 ] PAPEL (KEN)
[ 2 ] TESOURA (PÔ)""")
jogador = int(input('Qual é a sua jogada: '))
print(f'O computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
if computador == 0:
    if jogador == 0:
        print('EMPATAMOS! Vamos jogar novamente!')
    elif jogador == 1:
        print('PARABÉNS!!! Você conseguiu me vencer!')
    elif jogador == 2:
        print('QUE PENA! Eu ganhei!  Tente novamente.')
elif computador == 1:
    if jogador == 1:
        print('EMPATAMOS! Vamos jogar novamente!')
    elif jogador == 2:
        print('PARABÉNS!!! Você conseguiu me vencer!')
    elif jogador == 0:
        print('QUE PENA! Eu ganhei!  Tente novamente.')
elif computador == 2:
    if jogador == 2:
        print('EMPATAMOS! Vamos jogar novamente!')
    elif jogador == 0:
        print('PARABÉNS!!! Você conseguiu me vencer!')
    elif jogador == 1:
        print('QUE PENA! Eu ganhei!  Tente novamente.')