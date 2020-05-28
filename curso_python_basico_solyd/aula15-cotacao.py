import requests
import json
import time
import datetime

while True:
    requisicao = requests.get('https://economia.awesomeapi.com.br/all/USDT-BRL,EUR-BRL,BTC-BRL')

    cotacao = json.loads(requisicao.text)
    
    print('=-'*20)
    print(f'{"COTAÇÃO DO DIA":^40}', datetime.datetime.now())
    print('=-'*20)
    print('Dólar:', cotacao['USDT']['ask'])
    print('Euro:', cotacao['EUR']['ask'])
    print('Bitcoin:', cotacao['BTC']['ask'])
    print('=-'*20)
    time.sleep(4)