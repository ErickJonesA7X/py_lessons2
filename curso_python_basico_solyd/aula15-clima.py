import requests
import json
from googletrans import Translator
translator = Translator()

# t = translator.translate('food', dest='pt')
#
# print(t)

cidade = input(str('Escreva a sua cidade para saber o clima: ')).strip()

requisicao = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + cidade + '&APPID=ef4c1e254b5140e0ad875b939bec4ac0')

clima = json.loads(requisicao.text)
convert = clima['main']['temp'] - 273.15

condicao_tempo = str(clima['weather'][0]['main'])



print('Condição do tempo:', translator.translate(condicao_tempo, dest='pt'))
print('Temperatura:', f'{convert:.0f}°C')

# 302 K − 273,15 = 29,74 °C
# print(condicao_tempo)