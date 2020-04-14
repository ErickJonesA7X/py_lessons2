from datetime import date

dados = {}

dados['nome'] = str(input('Nome: '))
ano = int(input('Ano de Nascimento: '))
idade = date.today().year - ano
dados['idade'] = idade
dados['ctps'] = int(input('Carteira de trabalho (0 = não tem): '))
if dados['ctps'] == 0:
    print('-=' * 30)
    for k, v in dados.items():
        print(f'{k} tem o valor {v}.')
else:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = int(input('Salário: R$ '))
    dados['aposentadoria'] = (dados['contratação'] - ano) + 35
    print('-='*30)
    for k, v in dados.items():
        print(f'{k} tem o valor {v}')
