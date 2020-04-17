def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg} x {comp} é de {a}m².')



print('-'*30)
print('          CONTROLE DE TERRENOS')
print('-'*30)
l = float(input('Largura (m): '))
c= float(input('Comprimento (m): '))
área(l, c)