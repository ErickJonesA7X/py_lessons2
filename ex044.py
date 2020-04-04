preco = float(input('Digite o preço do produto: '))
print("""Qual condição de pagamento gostaria de fazer?
[ 1 ] À vista no dinheiro ou cheque: 10% de desconto.
[ 2 ] À vista no cartão: 5% de desconto.
[ 3 ] Em até 2x no cartão: Preço normal.
[ 4 ] 3x ou mais no cartão: 20% de juros.""")

escolha = int(input('Digite a sua opção: '))
if escolha == 1:
    desconto = preco - (preco*0.10)
    print(f'O valor original do produto de R${preco:.2f}, com 10% de desconto fica em R${desconto:.2f}')
elif escolha == 2:
    desconto = preco - (preco*0.05)
    print(f'O valor original do produto de R${preco:.2f}, com 5% de desconto fica em R${desconto:.2f}')
elif escolha == 3:
    print(f'O valor deste produto em 2x no cartão não possui descontos e fica em 2 parcelas de R${preco/2:.2f}')
elif escolha == 4:
    parcelas = int(input('Em quantas vezes deseja parcelar este produto: '))
    if parcelas >= 3:
        pfinal = (preco*0.20) + preco
        valorparcelas = pfinal / parcelas
        print(f"""O valor deste produto em {parcelas}x no cartão de crédito terá
        um acréscimo de 20% de juros e o valor final será de R${pfinal:.2f},
        e o valor de cada parcela por mês será de R${valorparcelas:.2f}""")
    else:
        print('Por favor digite novamente! Esta opção serve apenas para 3 ou mais parcelas.')
