nome = str(input('Digite seu nome completo: ')).strip()

print(f'Seu nome com todas as letras maiúsculas: {nome.upper()}')
print(f'Seu nome com todas as letras minúsculas: {nome.lower()}')
print(f'Seu nome tem {len(nome) - nome.count(" ")} letras.')
print(f'Seu primeiro nome tem {nome.find(" ")} letras.')