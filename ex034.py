salario = float(input('Digite o seu salário: '))

if salario <= 1250:
    print(f'O seu salário com reajusta de 15% ficou em R${(salario * 0.15) + salario:.2f}')
else:
    print(f'O seu salário com reajuste de 10% ficou em R${(salario*0.10) + salario:.2f}')
