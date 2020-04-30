
prim = int(input('Digite o 1st termo da PA: '))
razao = int(input('Digite a razão da PA: '))

n = prim + ((10 - 1) * razao)

for c in range(prim, n+1, razao):
    print(c, end=' -> ')
print('ACABOU!')