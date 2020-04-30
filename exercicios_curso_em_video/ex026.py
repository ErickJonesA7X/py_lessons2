frase = str(input('Escreva uma frase:')).upper()

print(f'A letra "a" aparece {frase.count("A")} vezes na frase.')
print(f'A primeira letra "a" apareceu pela primeira vez na {frase.find("A")+1}a posição.')
print(f'A última letra "a" apareceu na posição {frase.rfind("A")+1}°.')
