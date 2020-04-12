
num = (int(input('Digite um número: ')),
        int(input('Digite um número: ')),
        int(input('Digite um número: ')),
        int(input('Digite um número: ')))
print(f'Você digitou os valores {num}')

print(f'O número 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O número 3 apareceu pela primeira vez na {num.index(3)+1}ª posição.')
else:
    print(f'O número 3 não apareceu nenhuma vez.')
print(f'Dentre os números digitados, os pares são ', end='')
if num[0] % 2 == 0:
    print(num[0], end='')
    print(', ', end='')
if num[1] % 2 == 0:
    print(num[1], end='')
    print(', ', end='')
if num[2] % 2 == 0:
    print(num[2], end='')
    print(' e ', end='')
if num[3] % 2 == 0:
    print(num[3])