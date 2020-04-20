"""catO = float(input('Digite o valor do cateto oposto: '))
catA = float(input('Digite o valor do cateto adjacente: '))
hip = ((catO**2) + (catA**2)) ** (1/2)

print(f'O comprimento da hipotenusa no triangulo {catO}, {catA} é {hip:.2f}')"""

import math
catO = float(input('Digite o valor do cateto oposto: '))
catA = float(input('Digite o valor do cateto adjacente: '))
hi = math.hypot(catO, catA)
print(f'A hipotenusa deste triângulo vai medir {hi:.2f}')