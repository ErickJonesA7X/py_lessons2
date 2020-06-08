try:
    with open('nomes.txt', 'a') as arquivo:
        arquivo.write('João\n')
except Exception as error:
    print('Algum erro ocorreu')
    print(error)