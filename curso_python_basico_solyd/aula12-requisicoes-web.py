import requests

cabecalho = {'User-agent': 'Windows 12',
             'Refer': 'https://google.com'}

texto = None

try:
    requisicao = requests.post('https://putsreq.com/9tSzAmm6COu0Ue95AKfr',
                               headers=cabecalho)
    texto = requisicao.text
except Exception as e:
    print('Requisição deu erro:', e)

print(texto)