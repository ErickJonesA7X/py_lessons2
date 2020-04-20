from random import randint
from time import sleep

numeros = []

def sorteia():
    for c in range(0, 5):
        numeros.append(randint(1, 10))
    print(f'Sorteando 5 valores da lista: ', end='')
    for c in numeros:
        print(f'{c} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')


def soma():
    tot = 0
    for l, v in enumerate(numeros):
        if v % 2 == 0:
            tot += v
    print(f'Somando os valores pares de {numeros}, temos ', end='')
    print(f'{tot}.')


#Programa Principal
sorteia()
soma()