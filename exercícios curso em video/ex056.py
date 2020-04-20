tot = 0
media = 0
hmaisvelho = 0
nomemaisvelho = 0
for c in range(1, 5):
    print('----- {}ª PESSOA ------'.format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    media += idade
    if sexo == 'M':
        hmaisvelho = idade
        nomemaisvelho = nome
        if idade > hmaisvelho:
            hmaisvelho = idade
            nomemaisvelho = nome
    if sexo == 'F' and idade < 20:
        tot += 1
print(f'A média de idade do grupo é de {media/4} anos.')
print(f'O homem mais velho é o {nomemaisvelho} e ele tem {hmaisvelho} anos.')
print(f'Existe(m) {tot} mulher(es) com menos de 20 anos.')
