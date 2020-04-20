geral = []
pares = []
impares = []

while True:
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        if n not in pares:
            pares.append(n)
            geral.append(n)
    else:
        if n not in impares:
            impares.append(n)
            geral.append(n)
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if resp in 'N':
        break
print(f'Todos os números digitados foram {geral}')
print(f'Os valores pares digitados foram {pares}')
print(f'Os valores impares digitados foram {impares}')