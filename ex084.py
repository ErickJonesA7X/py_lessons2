
geral = []
dados = []
maior = menor = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(geral) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    geral.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if resp in 'N':
        break
print('=-'*30)
print(f'Ao todo, você cadastrou {len(geral)} pessoas.')
print(f'O maior peso cadastrado foi de {maior}kg. Peso de ', end='')
for p in geral:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso cadastrado foi de {menor}kg. Peso de ', end='')
for p in geral:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')