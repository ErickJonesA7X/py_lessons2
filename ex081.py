valores = []
cont = 0
while True:
    valores.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [S/N]: ')).strip().upper()
    cont += 1
    if r in 'N':
        break
print(valores)
valores.sort(reverse=True)
print(f'Você digitou {cont} elementos.')
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não foi encontrado na lista.')
