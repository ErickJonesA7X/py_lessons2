dados = {}
geral = []
somaidade = mediaidade = 0
mulheres = ''
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo: [M/F] ')).upper()
    if dados['sexo'] == 'F':
        mulheres += dados['nome'] + ' '
    dados['idade'] = int(input('Idade: '))
    continuar = str(input('Quer continuar? [S/N]: ')).upper()
    geral.append(dados.copy())
    somaidade += dados['idade']
    if continuar in 'N':
        break
mediaidade = somaidade / len(geral)
print('-='*30)
print(f'- O grupo tem {len(geral)} pessoas.')
print(f'- A média de idade é de {mediaidade:.1f} anos.')
print(f'- As mulheres cadastradas foram: {mulheres}')
print(f'- Lista das pessoas que estão acima da média de idade: \n')
for k, v in enumerate(geral):
    if v['idade'] > mediaidade:
        print(f'{v}')
print('<< ENCERRADO >>')