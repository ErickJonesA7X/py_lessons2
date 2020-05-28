import re
import requests


requisicao = requests.get('http://beljon.com.br/contato.html')

padrao = re.findall(r'\w+@\w+.\w+', requisicao.text)

if padrao:
    print(padrao)
else:
    print('Padrão não encontrado!')