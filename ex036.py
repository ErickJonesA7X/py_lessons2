valor = float(input('Qual o valor da casa que deseja comprar: '))
salario = float(input('Qual o seu salario: '))
prazo = int(input('Em quantos anos deseja pagar por esta casa: '))

trinta = salario * 0.30
meses = prazo * 12
parcela = valor / meses

if parcela <= trinta:
    print(f'O valor da prestação mensal de sua casa é de R${parcela:.2f}')
else:
    print(f'Infelizmente o valor da parcela ficou maior do que 30% do seu salário e não foi aprovada!')