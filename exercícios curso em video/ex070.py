loja = 'LOJA SUPER BARATÃO'
fim = 'FIM DO PROGRAMA'
print('='*30)
print(f'{loja:^30}')
print('='*30)
total = totmil = menor = cont = 0
barato = ''

while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    baratostr = ''
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'{fim:=^30}')
print(f'O total da compra foi de R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')