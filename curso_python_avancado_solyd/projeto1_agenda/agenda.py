AGENDA = {}  #Nome maiúsculo pra sinalizar que é uma variável global.
             #Pass = passar, deixa em "branco"

AGENDA['guilherme'] = {
    'telefone': '99928272',
    'email': 'guilherme@solyd.com.br',
    'endereco': 'av.1'
}

AGENDA['maria'] = {
    'telefone': '99922727',
    'email': 'maria@solyd.com.br',
    'endereco': 'av.2'
}

def mostrar_contatos():
    for contato in AGENDA:
        print("Nome:", contato)
        print('Telefone:', AGENDA[contato]['telefone'])
        print('Email:', AGENDA[contato]['email'])
        print('Endereço:', AGENDA[contato]['endereco'])
        print('=-='*20)


def buscar_contato(contato):
    print('Nome:', contato)
    print('Telefone:', AGENDA[contato]['telefone'])
    print('Email:', AGENDA[contato]['email'])
    print('Endereço:', AGENDA[contato]['endereco'])
    print(AGENDA[contato])


# mostrar_contatos()
buscar_contato('maria')