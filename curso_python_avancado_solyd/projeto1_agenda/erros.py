#Erros em tempo de compilação (Compile time errors)
#Erros em tempo de execução (Runtime Errors)
#Erros de lógica


try:
    a = float(input('Digite o número A: ')) #Value Error
    b = float(input('Digite o número B: '))

    print(a/b) #ZeroDivisionError
except ValueError as error:
    print('Input inválido, digite apenas números.')
except ZeroDivisionError as error:
    print('Não pode ser feita divisão por zero')
except Exception as error:
    print('Algum erro ocorreu')
    print(error)
finally:
    print('Fim do programa!')