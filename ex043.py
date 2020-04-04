peso = float(input('Digite o seu peso: '))
alt = float(input('Digite sua altura: '))

imc = peso / (alt * alt)
print(f'Seu IMC é de {imc:.2f}')

if imc < 18.5:
    print('Você está abaixo do seu peso!')
elif 18.5 <= imc < 25:
    print('Parabéns! Você está no seu peso ideal.')
elif 25 <= imc < 30:
    print('Cuidado, você está em sobrepeso.')
elif 30 <= imc < 40:
    print('CUIDADO! Você está obeso!')
else:
    print('PERIGO! Você está em obesidade mórbida!')