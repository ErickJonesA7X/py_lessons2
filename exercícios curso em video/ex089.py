geral = list()
alunos = list()
notas = list()
media = 0

while True:
    nome = str(input('Nome: ')).strip()
    n1 = float(input('Nota1: '))
    n2 = float(input('Nota2: '))
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()
    notas.append(n1)
    notas.append(n2)
    alunos.append(nome[:])
    alunos.append(notas[:])
    geral.append(alunos[:])
    notas.clear()
    alunos.clear()
    if resp in 'N':
        break
print('-=' * 30)
print('N°   NOME                MEDIA  ')
print('-' * 60)
for i, l in enumerate(geral):
    print(f'{i}    {l[0]:<10}          {(l[1][0] + l[1][1]) / 2:^1}')
while True:
    mostrar = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if mostrar == 999:
        break
    else:
        print(f'Notas de {geral[mostrar][0]} são {geral[mostrar][1]}')
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')