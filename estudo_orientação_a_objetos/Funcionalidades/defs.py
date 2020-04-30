

def cria_conta(numero=0, titular=0, saldo=0, limite=0):
    conta = {'numero': numero,
             'titular': titular,
             'saldo': saldo,
             'limite': limite}
    return conta


def deposita(conta, valor):
    conta['saldo'] += valor


def saca(conta, valor):
    conta['saldo'] -= valor


def extrato(conta):
    print("numero: {} \nsaldo: {}".format(conta['numero'], conta['saldo']))
