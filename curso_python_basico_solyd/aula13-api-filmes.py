import requests
import json


def requisicao(titulo):
    try:
        req = requests.get('http://www.omdbapi.com/?t=' + titulo + '&type=movie&apikey=d359a03b')
        dicionario = json.loads(req.text)
        return dicionario
    except:
        print('Erro na conexão')
        return None

def printar_detalhes(filme):
    print('Título:', filme['Title'])
    print('Ano:', filme['Year'])
    print('Diretor:', filme['Director'])
    print('Atores:', filme['Actors'])
    print('Nota:', filme['imdbRating'])
    print('Prêmios:', filme['Awards'])
    print('Pôster:', filme['Poster'])


sair = False
while not sair:
    op = input(str('Escreva o nome de um filme ou SAIR para fechar: ')).upper().strip()
    if op == 'SAIR':
        sair = True
    else:
        filme = requisicao(op)
        if filme['Response'] == False:
            print('Filme não encontrado!')
        else:
            printar_detalhes(filme)

print('Muito obrigado e volte sempre!')



