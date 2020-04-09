numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
            'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = 999

while True:
    while n < 0 or n > 20:
        n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        break
print(f'Você digitou o número {numeros[n]}.')