
valores = [[], []]

for v in range(1, 8):
    n = int(input(f'Digite o {v}° valor: '))
    if n % 2 == 0:
        valores[0].append(n)
    else:
        valores[1].append(n)
valores[0].sort()
valores[1].sort()
print('=-'*30)
print(f'Os valores pares digitados foram {valores[0]}.')
print(f'Os valores ímpares digitados foram {valores[1]}.')