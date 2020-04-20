from random import randint

valores = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(valores)

print(f'O menor valor é o {sorted(valores)[0]}.')
print(f'O maior valor é o {sorted(valores)[-1]}.')