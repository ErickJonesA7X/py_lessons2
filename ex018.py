import math

a = int(input('Digite um ângulo qualquer: '))
seno = math.sin(math.radians(a))
cosseno = math.cos((math.radians(a)))
tangente = math.tan(math.radians(a))

print(f'No ângulo {a} o valor do seu seno é {seno:.2f}, seu cosseno é {cosseno:.2f} e a tângente é {tangente:.2f}.')