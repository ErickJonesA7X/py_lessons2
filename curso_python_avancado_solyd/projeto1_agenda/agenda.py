AGENDA = {}  #Nome maiúsculo pra sinalizar que é uma variável global.
             #Pass = passar, deixa em "branco"


def mostrar_contatos():
    if AGENDA:
        for contato in AGENDA:
            print('*'*30)
            buscar_contato(contato)
            print('*'*30)
            print()
            print()
    else:
        print('Agenda vazia!')


def buscar_contato(contato):
    try:
        print('Nome:', contato)
        print('Telefone:', AGENDA[contato]['telefone'])
        print('Email:', AGENDA[contato]['email'])
        print('Endereço:', AGENDA[contato]['endereco'])
    except KeyError:
        print('Contato inexistente!')
    except Exception as error:
        print('Um erro inesperado aconteceu!')
        print(error)


def ler_detalhes_contato():
    telefone = input('Digite o número do telefone do contato: ')
    email = input('Digite o email do contato: ')
    endereco = input('Digite o endereço do contato: ')
    return telefone, email, endereco


def incluir_editar_contato(contato, telefone, email, endereco):
    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco
    }
    salvar()
    print()
    print(f'O contato {contato} foi adicionado/editado com sucesso!')
    print()


def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        salvar()
        print(f'O contato {contato} foi excluído.')
    except KeyError:
        print('Contato inexistente!')
    except Exception as error:
        print('Um erro inesperado aconteceu!')
        print(error)


def imprimir_menu():
    print('-=' *25)
    print(f'\t{"[ 1 ] Mostrar todos os contatos da agenda"}.')
    print(f'\t{"[ 2 ] Buscar contato da agenda"}.')
    print(f'\t{"[ 3 ] Incluir contato na agenda"}.')
    print(f'\t{"[ 4 ] Editar contato da agenda"}.')
    print(f'\t{"[ 5 ] Excluir contato da agenda"}.')
    print(f'\t{"[ 6 ] Exportar contatos para CSV"}.')
    print(f'\t{"[ 7 ] importar contatos CSV"}.')
    print(f'\t{"[ 0 ] Fechar agenda"}.')
    print('-=' * 25)
    print()



def exportar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'w') as arquivo:
            for contato in AGENDA:
                telefone = AGENDA[contato]['telefone']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                arquivo.write(f'{contato}, {telefone}, {email}, {endereco}\n')
        print('Agenda exportada com sucesso!')
    except Exception as error:
        print('Algum erro ocorreu ao exportar contatos!')
        print(error)


def importar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')

                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                incluir_editar_contato(nome, telefone, email, endereco)

    except FileNotFoundError:
        print('Arquivo não encontrado!!!')
    except Exception as error:
        print('Ocorreu um erro inesperado!')
        print(error)


def salvar():
    exportar_contatos('database.csv')


def carregar():
    try:
        with open('database.csv', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')

                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                AGENDA[nome] = {
                    'telefone': telefone,
                    'email': email,
                    'endereco': endereco
                }
        print('Database carregada com sucesso...')
        print(f'{len(AGENDA)} contatos carregados! ')
    except FileNotFoundError:
        print('Arquivo não encontrado!!!')
    except Exception as error:
        print('Ocorreu um erro inesperado!')
        print(error)




#INÍCIO DO PROGRAMA!
carregar()
while True:
    imprimir_menu()
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        mostrar_contatos()
    elif opcao == '2':
        buscar_contato(input(str('Digite o nome do contato que deseja buscar: ')))
    elif opcao == '3':
        contato = input('Digite o nome do contato que deseja incluir: ')

        try:
            AGENDA[contato]
            print('Contato já existente!')
        except KeyError:
            telefone, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(contato, telefone, email, endereco)
    elif opcao == '4':
        contato = input('Digite o nome do contato que deseja editar: ')

        try:
            AGENDA[contato]
            print('Editando o contato:', contato)
            telefone, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(contato, telefone, email, endereco)
        except KeyError:
            print('Contato inexistente!')
    elif opcao == '5':
        excluir_contato(input('Digite o nome do contato que deseja excluir: '))
    elif opcao == '6':
        nome_do_arquivo = input('Digite o nome do arquivo a ser exportado: ')
        exportar_contatos(nome_do_arquivo)
    elif opcao == '7':
        nome_do_arquivo = input('Digite o nome do arquivo a ser importado: ')
        importar_contatos(nome_do_arquivo)
    elif opcao == '0':
        break
    else:
        print('Opção inválida!!!   Por favor tente novamente...')

print('Encerrando PROGRAMA AGENDA...')