from ex109 import moeda

#Programa Principal
p = float(input('Digite um preço: R$ '))
print(f"A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}")
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Reduzindo 13%, temos {moeda.moeda(moeda.diminuir(p, 13))}')