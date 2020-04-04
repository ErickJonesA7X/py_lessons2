d = '='
n = 'TABUADA'
print(f'{n:=^40}')

num = int(input('Digite um número para saber a sua Tabuada: '))

for c in range(1, 11):
    print(f'{num:^10} x {c:^10} = {num*c:^10}')
print(f'{d*40:^40}')