from datetime import date

atual = date.today().year
tot = 0
tot2 = 0
for c in range(1, 8):
    ano = int(input('Digite o ano de nascimento da pessoa: '))
    idade = atual - ano
    if idade >= 21:
       tot += 1
    else:
        tot2 += 1
print(f'Das 7 pessoas, {tot} são maiores de idade e {tot2} são menores de idade.')