sexo = str(input('Informe o seu sexo: [M/F] ')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe o seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso!')