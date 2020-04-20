
primeiro = int(input('Digite o 1st termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro
cont  = 1
total = 0
mais = 10
while mais !=0:
    total = total + mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        cont+=1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar mais: '))
print('FIM!')