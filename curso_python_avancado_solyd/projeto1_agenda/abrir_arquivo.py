try:                                    #SEMPRE QUE FOR TENTAR ABRIR UM ARQUIVO USAR TRY/EXCEPT
    arquivo = open('emails.txt', 'w')
                                    ''' 
                                    Pesquisar no OPEN!
                                        R: Abre o arquivo para ler.
                                        W: Abre o arquivo em modo de escrita e cria ele na mesma pasta do arquivo.py 
                                        que o criou e o arquivo é sobescrito.
                                        B: Abre o arquivo em mondo binário (impossível ler)
                                        A: Modo apend.  Salva conteúdo incluído no arquivo sem apagar o anterior.'''
except FileNotFoundError:
    print('Arquivo não encontrado!')





# try:
#     with open('emails.txt') as arquivo:
#         print(arquivo.readlines())
# except FileNotFoundError:
#     print('O arquivo não existe!')