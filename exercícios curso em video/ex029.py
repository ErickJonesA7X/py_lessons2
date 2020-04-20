v = int(input('Digite a velocidade do carro: '))

if v > 80:
    print('VOCÊ FOI MULTADO!!!   Dirija com mais atenção!!!')
    print(f'O valor da sua multa é de R${(v - 80)*7}')
else:
    print('Parabéns, continue sendo prudente!')