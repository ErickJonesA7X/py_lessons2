import requests
import re



requisicao = requests.get('https://www.dolarhoje.net.br/dolar-turismo/')

padrao = re.findall(r'\w+\W\s\w\W\w+', requisicao.text)

if padrao:
    print(padrao)
else:
    print('Padrão não encontrado!')