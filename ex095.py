jogadores = list()
jogador = dict()
gols = list()


#       Area de captação dos dados


while True:
    gols.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for p in range(1, partidas + 1):
        gols.append(int(input(f'    Quantos gols na {p}ª partida? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())


    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while continuar not in 'SN':
        print('ERROR! Por favor, digite S ou N.')
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break


#       Mostrando Resultados


print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()


print('-' * 50)
for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 50)


#       Dados isolados


while True:
    escolha = int(input('Mostrar dados de qual jogador? (999 para encerrar): '))
    while escolha not in range(0, len(jogadores)) and escolha != 999:
        print('ERROR! Não existe jogador com este código.')
        print('-' * 50)
        escolha = int(input('Mostrar dados de qual jogador? (999 para encerrar): '))
    if escolha == 999:
        break
    print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[escolha]["nome"]}')
    for i, v in enumerate(jogadores[escolha]['gols']):
        print(f'    No jogo {i + 1} fez {v} gols.')
    print('-' * 50)
print('<<< PROGRAMA ENCERRADO >>>')