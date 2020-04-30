import requests

class Pessoa:
    nome = ''
    idade = ''
    telefone = ''
    endereco = ''

    def apresentacao(self):
        print(f'Meu nome é {self.nome}')



class Funcionario(Pessoa):
    cargo = ''

    def apresentacao(self):
        print(f'Meu nome é {self.nome}. Eu sou o {self.cargo} da empresa X')

f1 = Funcionario()

f1.nome = 'João'
f1.cargo = 'Motorista'
f1.apresentacao()



# print(Pessoa)
#
p1 = Pessoa()
# print(p1)
# print(p1.nome)
p1.nome = 'Érick'
# print(p1.nome)
#
p1.apresentacao()