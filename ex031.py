dist = float(input('Digite a distância da viagem que irá fazer: '))

if dist <= 200:
    print(f'O valor da sua passagem é de R${dist*0.50:.2f}')
else:
    print(f'O valor da sua passagem é de R${dist*0.45:.2f}')