
prim = int(input('Digite o 1st termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = prim
cont  = 1
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    cont+=1
print('Fim!')