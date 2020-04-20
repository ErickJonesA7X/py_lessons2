r1 = int(input('Digite o valor da primeira reta de um triângulo: '))
r2 = int(input('Digite o valor da segunda reta de um triângulo: '))
r3 = int(input('Digite o valor da terceira reta de um triângulo: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Sim! As retas acima PODEM FORMAR um triângulo.')
    if r1 == r2 == r3:
        print('Este é um triângulo EQUILÁTERO.')
    if r1 == r2 and r2 != r3:
        print('Este é um triângulo ISÓSCELES.')
    if r1 != r2 != r3:
        print('Este é um triângulo ESCALENO.')
else:
    print('As retas acima NÃO PODEM formar um triângulo!')