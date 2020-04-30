# print()
# len()

# def soma(numero1, numero2):
#     resp = numero1 + numero2
#     return resp
#
# print(soma(4, 8))


# def tem_sete_itens(argumento):
#     if len(argumento) == 7:
#         return True
#     else:
#         return False
#
#
# print(tem_sete_itens('Sete le'))


def maior_valor(list=[]):
    maior = 0
    menor = 9999  #Gambiarra  o certo é criar uma outra função para o menor número e fazer o menor começando pelo primeiro item da lista.
    for c in list:
        if c > maior:
            maior = c
        if c < menor:
            menor = c
    print(maior, menor)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 15, 1000]

maior_valor(lista)