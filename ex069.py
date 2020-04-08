titulo = 'CADASTRE UMA PESSOA'
print('-'*30)
print(f'{titulo:^30}')
print('-'*30)
tot18 = 0
homem = 0
mulher20 = 0


while True:
    idade = int(input('Idade: '))
    if idade > 18:
        tot18 += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if sexo in 'M':
            homem += 1
        if sexo in 'F' and idade < 20:
            mulher20 +=1
    print('-' * 30)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {homem} homens cadastrados.')
print(f'E temos {mulher20} mulher(es) com menos de 20 anos.')