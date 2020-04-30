import sys

argumentos = sys.argv #arg1 metod // arg2 - n1 // arg3 - n2



def soma(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


if argumentos[1] == "soma":
    resp = soma(argumentos[2], argumentos[3])
