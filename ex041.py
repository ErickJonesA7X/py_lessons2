from datetime import date
nasc = int(input('Digite a data de nascimento do atleta: '))

atual = date.today().year - nasc

if atual <= 9:
    print(f'A categoria deste atleta é MIRIM!')
elif 9 < atual <= 14:
    print('A categoria deste atleta é INFANTIL!')
elif 14 < atual <= 19:
    print('A categoria deste atleta é JUNIOR!')
elif 19 < atual <= 20:
    print('A categoria deste atleta é SÊNIOR!')
else:
    print('A categoria deste atleta é MASTER!')