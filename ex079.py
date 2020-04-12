valores = []
resp = ' '

while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não irei adicionar...')
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if resp in 'N':
        break
print('=-'*30)
print(f'Você digitou os valores {valores}')