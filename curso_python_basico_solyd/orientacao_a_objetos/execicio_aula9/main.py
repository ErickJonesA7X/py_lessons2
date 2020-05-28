from curso_python_basico_solyd.orientacao_a_objetos.execicio_aula9.conta import *


cliente1 = Cliente('Érick', '119.049.167-24', 30)

conta_do_erick = Conta(cliente1, 1000, 1000)

print(cliente1)

print(conta_do_erick.cliente.nome, conta_do_erick.consulta_saldo())

conta_do_erick.depositar(1000)
print(conta_do_erick.consulta_saldo())

conta_do_erick.sacar(3000)
print(conta_do_erick.consulta_saldo())




# print(conta_do_erick.consulta_saldo())
#
# conta_do_erick.sacar(500)
#
# print(conta_do_erick.consulta_saldo())
#
# conta_do_erick.depositar(5)
#
# print(conta_do_erick.consulta_saldo())
#
# conta_do_erick.sacar(1000)
#
# print(conta_do_erick.consulta_saldo())
#
# conta_do_erick.sacar(10000)
#
# conta_do_erick.consulta_saldo()