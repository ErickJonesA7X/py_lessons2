n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))

media = (n1+n2) / 2

if media < 5.0:
    print(f'Sua média final é {media} e você está REPROVADO!')
elif 5.0 <= media <= 6.9:
    print(f'Sua média final é {media} e você está de RECUPERAÇÃO!')
else:
    print(f'PARABÉNS!!!  Você está APROVADO!')