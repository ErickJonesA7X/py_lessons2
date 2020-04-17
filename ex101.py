def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - nasc
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL!'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'

#Programa Principal
nasc = int(input('Digite o ano do seu nascimento: '))
print(voto(nasc))