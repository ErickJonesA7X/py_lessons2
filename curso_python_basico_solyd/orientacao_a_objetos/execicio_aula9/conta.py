from curso_python_basico_solyd.orientacao_a_objetos.execicio_aula9.cliente import *

class Conta(Cliente):

    def __init__(self, cliente, saldo):
        self.cliente = cliente
        self.saldo = saldo


    def Sacar(self, valor_a_sacar):
        if valor_a_sacar <= saldo:
            saldo -= valor_a_sacar
            print(f'Você sacou {valor_a_sacar} e seu saldo atual é {saldo}')
        else:
            print('ERRO!  Você não tem saldo suficiente para esta operação.')