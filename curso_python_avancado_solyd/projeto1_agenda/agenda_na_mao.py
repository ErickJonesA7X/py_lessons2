AGENDA = {
    'guilherme': {
        'tel': '99999-1010',
        'email': 'contato@solyd.com.br',
        'endereco': 'av.1'
    },
    'maria': {
        'tel': '99999-2020',
        'email': 'maria@solyd.com.br',
        'endereco': 'av.2'
    },
    'joao': {
        'tel': '99999-6060',
        'email': 'joao@solyd.com.br',
        'endereco': 'av.3'
    },
    'erick': {
        'tel': '98001-8646',
        'email': 'jonescomercial@gmail.com',
        'endereco': 'rua tejo, 45'
    }
}


cadastro_nome = input(str('Bem vindo ao cadastro!  Digite seu nome primeiramente para se cadastrar: ')).strip().lower()
cadastro_tel = input(str('Digite agora o seu telefone: ')).strip().lower()
cadastro_email = input(str('Digite agora o seu email: ')).strip().lower()
cadastro_endereco = input(str('Digite por último o seu endereço: ')).strip().lower()

AGENDA[cadastro_nome] = {'tel': cadastro_tel, 'email': cadastro_email, 'endereco': cadastro_endereco}

while True:
    consulta = input(str('Digite o nome da pessoa que você quer consultar: ')).strip().lower()
    item = input(str('Digite o que você quer consultar dessa pessoa: ')).strip().lower()
    print(AGENDA[consulta][item])
    cont = input(str('Quer continuar? [S/N]: ')).strip().upper()
    if cont in 'nN':
        break
print('Muito obrigado pela sua consulta!')