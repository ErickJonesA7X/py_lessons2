soma = 0
tot = 0
for c in range(1, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma += n
        tot += 1
print(f'Você me informou {tot} números pares e a soma deles é {soma}')