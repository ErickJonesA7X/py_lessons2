cont = 0
soma = 0
n = 0

while n != 999:
    n = int(input('Digite um número! Se quiser parar digite 999: '))
    cont += 1
    soma += n
    if n == 999:
        soma = soma - 999
        cont = cont - 1
print(f'Foram digitados {cont} números e a soma deles é de {soma}.')