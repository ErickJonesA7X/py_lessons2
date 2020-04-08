from random import randint

print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR ?!')
print('=-'*15)
result = ''
cont = 0

while True:
    jogador = int(input('Diga um valor: '))
    pi = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()
    computador = randint(0, 10)
    soma = computador + jogador
    parouimpar = soma % 2
    if parouimpar == 0:
        result = 'Par'
    else:
        result = 'Ímpar'
    print('-'*30)
    print(f'Você jogou o {jogador} e o computador {computador}. Total de {soma} deu {result}.')
    print('-' * 30)
    if parouimpar == 0 and pi == 'P':
        print(f"""Você VENCEU!
Vamos jogar novamente...""")
    if parouimpar != 0 and pi == 'I':
        print(f"""Você VENCEU!
Vamos jogar novamente...""")
    if parouimpar == 0 and pi == 'I':
        print(f'Você PERDEU!')
        break
    if parouimpar != 0 and pi == 'P':
        print(f'Você PERDEU!')
        break
    cont += 1
print('=-'*15)
print(f'GAME OVER! Você venceu {cont} vezes')