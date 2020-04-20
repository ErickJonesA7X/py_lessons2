
r = 0
soma = 0
cont = 0
menor = 0
maior = 0
n = 0

while r != 'N':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    media = soma / cont
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    r = str(input('Você quer continuar? [S/N]: ')).strip().upper()
print(f'Você digitou {cont} números.')
print(f'A soma entre eles é {soma}')
print(f'O maior número digitado foi {maior}')
print(f'O menor número digitado foi {menor}')
print(f'E a média aritmética entre eles é de {media}')
