conjunto_cores = {'vermelho', 'azul', 'verde'}  #O conjunto (set) não é ordenado assim como o dicionário.
                                                #Logo, o conjunto não tem index, e é geralmente acessado pelo "For"
                                                #Para adicionar itens ao conjunto utilizar o comando "add".



conjunto_cores.add('roxo')
conjunto_cores.remove('verde')


for cor in conjunto_cores:
    print(cor)