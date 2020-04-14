dados = {}
partidas =[]
tot = soma = 0

dados['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {dados["nome"]} jogou: '))

for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols na partida {c}: ')))
dados['gols'] = partidas[:]
for c in dados['gols']:
    soma += c
dados['total'] = soma
print('=-'*30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}.')
print('=-'*30)
print(f'O jogador {dados["nome"]} jogou {tot} partidas.')
for k, v in enumerate(partidas):
    print(f'  => Na partida {k}, fez {v} gols.')
print(f'Foi um total de {soma} gols.')