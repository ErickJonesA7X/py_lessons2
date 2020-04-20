n = 0
cont = 0
while True:
    n = int(input('Quer ver a tabuada de qual número: '))
    if n < 0:
        break
    print('-' * 30)
    for c in range(1, 11):
        cont += 1
        print(f'{n} x {c} = {n * c}')
    print('-' * 30)
print('PROGRAMA TABOADA ENCERRADO! VOLTE SEMPRE!')