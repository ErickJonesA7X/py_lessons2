opc = 0
n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))


while opc != 5:
    opc = int(input("""O que você deseja fazer com esses 2 números?
    [ 1 ] Somar
    [ 2 ] multiplicar
    [ 3 ] descobrir qual é o maior
    [ 4 ] digitar novos números
    [ 5 ] sair do programa
    Qual a sua opção: """))
    print('=-=' * 15)
    if opc == 1:
        print(f'A soma entre {n1} e {n2} é {n1+n2}.')
        print('=-=' * 15)
    elif opc == 2:
        print(f'{n1} multiplicado por {n2} é {n1*n2}')
        print('=-=' * 15)
    elif opc == 3:
        if n1 > n2:
            print(f'O maior número entre eles é o {n1}.')
            print('=-=' * 15)
        if n2 > n1:
            print(f'O maior número entre eles é o {n2}')
            print('=-=' * 15)
    elif opc == 4:
        print('Informe os números novamente...')
        n1 = int(input('Digite o 1° número: '))
        n2 = int(input('Digite o 2° número: '))
        print('=-=' * 15)
print('FIM!')
